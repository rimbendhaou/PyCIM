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

from CIM14v13.IEC61970.Core.Curve import Curve

class StartRampCurve(Curve):
    """Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line
    """

    def __init__(self, hotStandbyRamp=0.0, StartupModel=None, *args, **kw_args):
        """Initializes a new 'StartRampCurve' instance.

        @param hotStandbyRamp: The startup ramp rate in gross for a unit that is on hot standby 
        @param StartupModel: The unit's startup model may have a startup ramp curve
        """
        #: The startup ramp rate in gross for a unit that is on hot standby
        self.hotStandbyRamp = hotStandbyRamp

        self._StartupModel = None
        self.StartupModel = StartupModel

        super(StartRampCurve, self).__init__(*args, **kw_args)

    def getStartupModel(self):
        """The unit's startup model may have a startup ramp curve
        """
        return self._StartupModel

    def setStartupModel(self, value):
        if self._StartupModel is not None:
            self._StartupModel._StartRampCurve = None

        self._StartupModel = value
        if self._StartupModel is not None:
            self._StartupModel._StartRampCurve = self

    StartupModel = property(getStartupModel, setStartupModel)

