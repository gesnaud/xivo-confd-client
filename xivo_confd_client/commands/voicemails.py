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

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import UserVoicemailRelation


class VoicemailRelation(object):

    def __init__(self, builder, voicemail_id):
        self.voicemail_id = voicemail_id
        self.user_voicemail_relation = UserVoicemailRelation(builder)

    @extract_id
    def add_user(self, user_id):
        self.user_voicemail_relation.associate(user_id, self.voicemail_id)

    @extract_id
    def remove_user(self, user_id):
        self.user_voicemail_relation.dissociate(user_id)

    def remove_users(self):
        response = self.list_users()
        for association in response['items']:
            self.remove_user(association['user_id'])

    def list_users(self):
        return self.user_voicemail_relation.list_by_voicemail(self.voicemail_id)


class VoicemailsCommand(CRUDCommand):

    resource = 'voicemails'

    relation_cmd = VoicemailRelation
