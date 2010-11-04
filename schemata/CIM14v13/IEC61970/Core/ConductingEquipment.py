# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.Equipment import Equipment

class ConductingEquipment(Equipment):
    """The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """

    def __init__(self, phases='BC', Terminals=None, ClearanceTags=None, OutageStepRoles=None, BaseVoltage=None, ElectricalAssets=None, SvStatus=None, ProtectionEquipments=None, *args, **kw_args):
        """Initializes a new 'ConductingEquipment' instance.

        @param phases: Describes the phases carried by a conducting equipment. Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        @param Terminals: ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        @param ClearanceTags: Conducting equipment may have multiple clearance tags for authorized field work
        @param OutageStepRoles:
        @param BaseVoltage: Use association to ConductingEquipment only when there is no VoltageLevel container used.
        @param ElectricalAssets:
        @param SvStatus: The status state associated with the conducting equipment.
        @param ProtectionEquipments: Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        """
        #: Describes the phases carried by a conducting equipment.Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        self.phases = phases

        self._Terminals = []
        self.Terminals = [] if Terminals is None else Terminals

        self._ClearanceTags = []
        self.ClearanceTags = [] if ClearanceTags is None else ClearanceTags

        self._OutageStepRoles = []
        self.OutageStepRoles = [] if OutageStepRoles is None else OutageStepRoles

        self._BaseVoltage = None
        self.BaseVoltage = BaseVoltage

        self._ElectricalAssets = []
        self.ElectricalAssets = [] if ElectricalAssets is None else ElectricalAssets

        self._SvStatus = None
        self.SvStatus = SvStatus

        self._ProtectionEquipments = []
        self.ProtectionEquipments = [] if ProtectionEquipments is None else ProtectionEquipments

        super(ConductingEquipment, self).__init__(*args, **kw_args)

    def getTerminals(self):
        """ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        """
        return self._Terminals

    def setTerminals(self, value):
        for x in self._Terminals:
            x._ConductingEquipment = None
        for y in value:
            y._ConductingEquipment = self
        self._Terminals = value

    Terminals = property(getTerminals, setTerminals)

    def addTerminals(self, *Terminals):
        for obj in Terminals:
            obj._ConductingEquipment = self
            self._Terminals.append(obj)

    def removeTerminals(self, *Terminals):
        for obj in Terminals:
            obj._ConductingEquipment = None
            self._Terminals.remove(obj)

    def getClearanceTags(self):
        """Conducting equipment may have multiple clearance tags for authorized field work
        """
        return self._ClearanceTags

    def setClearanceTags(self, value):
        for x in self._ClearanceTags:
            x._ConductingEquipment = None
        for y in value:
            y._ConductingEquipment = self
        self._ClearanceTags = value

    ClearanceTags = property(getClearanceTags, setClearanceTags)

    def addClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj._ConductingEquipment = self
            self._ClearanceTags.append(obj)

    def removeClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj._ConductingEquipment = None
            self._ClearanceTags.remove(obj)

    def getOutageStepRoles(self):
        
        return self._OutageStepRoles

    def setOutageStepRoles(self, value):
        for x in self._OutageStepRoles:
            x._ConductingEquipment = None
        for y in value:
            y._ConductingEquipment = self
        self._OutageStepRoles = value

    OutageStepRoles = property(getOutageStepRoles, setOutageStepRoles)

    def addOutageStepRoles(self, *OutageStepRoles):
        for obj in OutageStepRoles:
            obj._ConductingEquipment = self
            self._OutageStepRoles.append(obj)

    def removeOutageStepRoles(self, *OutageStepRoles):
        for obj in OutageStepRoles:
            obj._ConductingEquipment = None
            self._OutageStepRoles.remove(obj)

    def getBaseVoltage(self):
        """Use association to ConductingEquipment only when there is no VoltageLevel container used.
        """
        return self._BaseVoltage

    def setBaseVoltage(self, value):
        if self._BaseVoltage is not None:
            filtered = [x for x in self.BaseVoltage.ConductingEquipment if x != self]
            self._BaseVoltage._ConductingEquipment = filtered

        self._BaseVoltage = value
        if self._BaseVoltage is not None:
            self._BaseVoltage._ConductingEquipment.append(self)

    BaseVoltage = property(getBaseVoltage, setBaseVoltage)

    def getElectricalAssets(self):
        
        return self._ElectricalAssets

    def setElectricalAssets(self, value):
        for x in self._ElectricalAssets:
            x._ConductingEquipment = None
        for y in value:
            y._ConductingEquipment = self
        self._ElectricalAssets = value

    ElectricalAssets = property(getElectricalAssets, setElectricalAssets)

    def addElectricalAssets(self, *ElectricalAssets):
        for obj in ElectricalAssets:
            obj._ConductingEquipment = self
            self._ElectricalAssets.append(obj)

    def removeElectricalAssets(self, *ElectricalAssets):
        for obj in ElectricalAssets:
            obj._ConductingEquipment = None
            self._ElectricalAssets.remove(obj)

    def getSvStatus(self):
        """The status state associated with the conducting equipment.
        """
        return self._SvStatus

    def setSvStatus(self, value):
        if self._SvStatus is not None:
            self._SvStatus._ConductingEquipment = None

        self._SvStatus = value
        if self._SvStatus is not None:
            self._SvStatus._ConductingEquipment = self

    SvStatus = property(getSvStatus, setSvStatus)

    def getProtectionEquipments(self):
        """Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        """
        return self._ProtectionEquipments

    def setProtectionEquipments(self, value):
        for p in self._ProtectionEquipments:
            filtered = [q for q in p.ConductingEquipments if q != self]
            self._ProtectionEquipments._ConductingEquipments = filtered
        for r in value:
            if self not in r._ConductingEquipments:
                r._ConductingEquipments.append(self)
        self._ProtectionEquipments = value

    ProtectionEquipments = property(getProtectionEquipments, setProtectionEquipments)

    def addProtectionEquipments(self, *ProtectionEquipments):
        for obj in ProtectionEquipments:
            if self not in obj._ConductingEquipments:
                obj._ConductingEquipments.append(self)
            self._ProtectionEquipments.append(obj)

    def removeProtectionEquipments(self, *ProtectionEquipments):
        for obj in ProtectionEquipments:
            if self in obj._ConductingEquipments:
                obj._ConductingEquipments.remove(self)
            self._ProtectionEquipments.remove(obj)

