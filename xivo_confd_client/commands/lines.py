# -*- coding: utf-8 -*-

# Copyright (C) 2015 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from xivo_confd_client.crud import CRUDCommand


class LinesCommand(CRUDCommand):

    resource = 'lines'

    def create(self, body):
        raise NotImplementedError("Command is not implemented")

    def update(self, body):
        raise NotImplementedError("Command is not implemented")

    def delete(self, resource_or_id):
        raise NotImplementedError("Command is not implemented")