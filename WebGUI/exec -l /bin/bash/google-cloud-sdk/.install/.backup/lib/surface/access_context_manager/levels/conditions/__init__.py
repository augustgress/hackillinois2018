# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The command group for the Access Context Manager levels CLI."""
from googlecloudsdk.calliope import base


class LevelCondition(base.Group):
  """Manage Access Context Manager level conditions.

  An access level is a classification of requests based on raw attributes of
  that request (e.g. IP address, device identity, time of day, etc.). These
  individual attributes are called conditions.
  """
