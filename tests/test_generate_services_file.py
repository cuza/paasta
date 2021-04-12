# Copyright 2015-2016 Yelp Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import socket
from unittest import mock

import pytest

from paasta_tools import generate_services_file


MOCK_NAMESPACES = [
    ("foo.main", {"proxy_port": 1024}),
    ("bar.canary", {"proxy_port": 1025}),
]


@pytest.yield_fixture
def mock_namespaces():
    with mock.patch(
        "paasta_tools.generate_services_file.get_all_namespaces",
        autospec=True,
        return_value=MOCK_NAMESPACES,
    ):
        yield


def test_generate_configuration(mock_namespaces):
    expected = {
        "foo.main": {"host": "169.254.255.254", "port": 1024},
        "bar.canary": {"host": "169.254.255.254", "port": 1025},
    }
    assert expected == generate_services_file.generate_configuration()


@mock.patch("paasta_tools.generate_services_file.parse_args", autospec=True)
@mock.patch.object(socket, "getfqdn", return_value="somehost.yelp", autospec=True)
def test_main_yaml(mock_getfqdn, mock_parse_args, tmpdir, mock_namespaces):
    services_file = tmpdir.join("services.yaml")
    fake_args = mock.Mock()
    fake_args.output_format = "yaml"
    fake_args.output_filename = services_file.strpath
    mock_parse_args.return_value = fake_args

    expected_value = (
        "# This file is automatically generated by paasta_tools.\n"
        "# It was automatically generated at $TIME on somehost.yelp.\n"
        "---\n"
        "bar.canary:\n"
        "  host: 169.254.255.254\n"
        "  port: 1025\n"
        "foo.main:\n"
        "  host: 169.254.255.254\n"
        "  port: 1024\n"
    )

    with mock.patch.object(generate_services_file, "datetime") as m:
        m.now().isoformat.return_value = "$TIME"
        generate_services_file.main()
    assert services_file.read() == expected_value

    # If the only difference is the timestamp, the file should not be regenerated.
    with mock.patch.object(generate_services_file, "datetime") as m:
        m.now().isoformat.return_value = "$TIME+1"
        generate_services_file.main()
    assert services_file.read() == expected_value


@mock.patch("paasta_tools.generate_services_file.parse_args", autospec=True)
def test_main_json(mock_parse_args, tmpdir, mock_namespaces):
    services_file = tmpdir.join("services.json")
    fake_args = mock.Mock()
    fake_args.output_format = "json"
    fake_args.output_filename = services_file.strpath
    mock_parse_args.return_value = fake_args

    generate_services_file.main()

    assert (
        services_file.read()
        == """{
  "bar.canary": {
    "host": "169.254.255.254",
    "port": 1025
  },
  "foo.main": {
    "host": "169.254.255.254",
    "port": 1024
  }
}"""
    )
