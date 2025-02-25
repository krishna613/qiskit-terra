# This code is part of Qiskit.
#
# (C) Copyright IBM 2021, 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Interface for Quantum Real Time Evolution."""

from abc import ABC, abstractmethod
from qiskit.utils.deprecation import deprecate_func

from .evolution_problem import EvolutionProblem
from .evolution_result import EvolutionResult


class RealEvolver(ABC):
    """Pending deprecation: Interface for Quantum Real Time Evolution.

    The RealEvolver interface has been superseded by the
    :class:`qiskit.algorithms.time_evolvers.RealTimeEvolver` interface.
    This interface will be deprecated in a future release and subsequently
    removed after that.

    """

    @deprecate_func(
        additional_msg=(
            "Instead, use the interface ``qiskit.algorithms.time_evolvers.RealTimeEvolver``"
        ),
        since="0.23.0",
        pending=True,
    )
    def __init__(self) -> None:
        pass

    @abstractmethod
    def evolve(self, evolution_problem: EvolutionProblem) -> EvolutionResult:
        r"""Perform real time evolution :math:`\exp(-i t H)|\Psi\rangle`.

        Evolves an initial state :math:`|\Psi\rangle` for a time :math:`t`
        under a Hamiltonian  :math:`H`, as provided in the ``evolution_problem``.

        Args:
            evolution_problem: The definition of the evolution problem.

        Returns:
            Evolution result which includes an evolved quantum state.
        """
        raise NotImplementedError()
