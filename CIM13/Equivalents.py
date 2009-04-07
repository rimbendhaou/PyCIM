#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM13.Core import ConnectivityNodeContainer
from CIM13.Core import ConductingEquipment



from enthought.traits.api import Instance, List, Float
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "EquivalentNetwork" class:
#------------------------------------------------------------------------------

class EquivalentNetwork(ConnectivityNodeContainer):
    """ A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    EquivalentEquipments = List(Instance("CIM13.Equivalents.EquivalentEquipment"))

    #--------------------------------------------------------------------------
    #  Begin equivalentNetwork user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equivalentNetwork user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentEquipment" class:
#------------------------------------------------------------------------------

class EquivalentEquipment(ConductingEquipment):
    """ The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    EquivalentNetwork = Instance("CIM13.Equivalents.EquivalentNetwork")

    #--------------------------------------------------------------------------
    #  Begin equivalentEquipment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equivalentEquipment user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentBranch" class:
#------------------------------------------------------------------------------

class EquivalentBranch(EquivalentEquipment):
    """ The class represents equivalent branches.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence series reactance of the reduced branch.
    x = EFloat

    # Positive sequence series resistance of the reduced branch.
    r = EFloat

    #--------------------------------------------------------------------------
    #  Begin equivalentBranch user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equivalentBranch user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentShunt" class:
#------------------------------------------------------------------------------

class EquivalentShunt(EquivalentEquipment):
    """ The class represents equivalent shunts.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence shunt conductance.
    g = EFloat

    # Positive sequence shunt susceptance.
    b = EFloat

    #--------------------------------------------------------------------------
    #  Begin equivalentShunt user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equivalentShunt user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------