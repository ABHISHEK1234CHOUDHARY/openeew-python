# =============================================================================
# Copyright 2019 Grillo Holdings Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

import pytest
from openeew.data.aws import AwsDataClient


def test_initialize_country_code_all_caps():

    data_client = AwsDataClient('AB')

    assert data_client.country_code == 'ab'


def test_change_country_code_all_caps():

    data_client = AwsDataClient('AB')
    data_client.country_code = 'CD'

    assert data_client.country_code == 'cd'
