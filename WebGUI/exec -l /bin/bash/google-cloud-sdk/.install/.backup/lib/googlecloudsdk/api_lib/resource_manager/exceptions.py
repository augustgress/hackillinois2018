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
"""Wrapper for user-visible error exceptions to raise in the CLI."""

from googlecloudsdk.core import exceptions


class ResourceManagerError(exceptions.Error):
  """Exceptions for Resource Manager errors."""


class ResourceManagerInputFileError(ResourceManagerError):
  """More specific errors for failure to read input files."""


class ArgumentError(ResourceManagerError):
  """Command argument error."""
