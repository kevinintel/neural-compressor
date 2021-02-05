# -*- coding: utf-8 -*-
# Copyright (c) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""LPOT configuration tuning module."""

from typing import Any, Dict, Optional

from lpot.ux.utils.json_serializer import JsonSerializer


class Strategy(JsonSerializer):
    """LPOT configuration Strategy class."""

    def __init__(self, data: Dict[str, Any] = {}) -> None:
        """Initialize LPOT configuration Strategy class."""
        super().__init__()
        # [Required] One of lpot.strategy.STRATEGIES
        self.name: str = data.get("name", "basic")

        self.accuracy_weight: Optional[float] = data.get("accuracy_weight", None)
        self.latency_weight: Optional[float] = data.get("latency_weight", None)


class AccCriterion(JsonSerializer):
    """LPOT configuration AccCriterion class."""

    def __init__(self, data: Dict[str, Any] = {}) -> None:
        """Initialize LPOT configuration Strategy class."""
        super().__init__()
        self.relative: Optional[float] = data.get(
            "relative",
            None,
        )  # [Optional] (INT8-FP32)/FP32
        self.absolute: Optional[float] = data.get(
            "absolute",
            None,
        )  # [Optional] INT8-FP32


class ExitPolicy(JsonSerializer):
    """LPOT configuration ExitPolicy class."""

    def __init__(self, data: Dict[str, Any] = {}) -> None:
        """Initialize LPOT configuration ExitPolicy class."""
        super().__init__()
        self.timeout: Optional[int] = data.get("timeout", None)

        self.max_trials: Optional[int] = data.get("max_trials", None)


class Workspace(JsonSerializer):
    """LPOT configuration Workspace class."""

    def __init__(self, data: Dict[str, Any] = {}) -> None:
        """Initialize LPOT configuration Workspace class."""
        super().__init__()
        self.path: Optional[str] = data.get("path", None)  # [Optional]

        self.resume: Optional[str] = data.get("resume", None)  # [Optional]


class Tuning(JsonSerializer):
    """LPOT configuration Tuning class."""

    def __init__(self, data: Dict[str, Any] = {}) -> None:
        """Initialize LPOT configuration Tuning class."""
        super().__init__()
        self.strategy: Strategy = Strategy()  # [Optional]
        if data.get("strategy"):
            self.strategy = Strategy(data.get("strategy", {}))

        self.accuracy_criterion: AccCriterion = AccCriterion(
            data.get("accuracy_criterion", {}),
        )

        # [Optional] One of lpot.objective.OBJECTIVES
        self.objective: Optional[str] = data.get("objective", None)

        self.exit_policy: Optional[ExitPolicy] = None  # [Optional]
        if data.get("exit_policy"):
            self.exit_policy = ExitPolicy(data.get("exit_policy", {}))

        self.random_seed: Optional[int] = data.get("random_seed", None)

        self.tensorboard: Optional[bool] = data.get("tensorboard", None)

        self.workspace: Workspace = Workspace(data.get("workspace", {}))