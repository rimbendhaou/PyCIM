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

from CIM14v13.IEC61970.Meas.Limit import Limit

class AccumulatorLimit(Limit):
    """Limit values for Accumulator measurements
    """

    def __init__(self, value=0, LimitSet=None, *args, **kw_args):
        """Initializes a new 'AccumulatorLimit' instance.

        @param value: The value to supervise against. The value is positive. 
        @param LimitSet: The set of limits.
        """
        #: The value to supervise against. The value is positive.
        self.value = value

        self._LimitSet = None
        self.LimitSet = LimitSet

        super(AccumulatorLimit, self).__init__(*args, **kw_args)

    def getLimitSet(self):
        """The set of limits.
        """
        return self._LimitSet

    def setLimitSet(self, value):
        if self._LimitSet is not None:
            filtered = [x for x in self.LimitSet.Limits if x != self]
            self._LimitSet._Limits = filtered

        self._LimitSet = value
        if self._LimitSet is not None:
            self._LimitSet._Limits.append(self)

    LimitSet = property(getLimitSet, setLimitSet)

