
# UrbanFootprint v1.5
# Copyright (C) 2016 Calthorpe Analytics
#
# This file is part of UrbanFootprint version 1.5
#
# UrbanFootprint is distributed under the terms of the GNU General
# Public License version 3, as published by the Free Software Foundation. This
# code is distributed WITHOUT ANY WARRANTY, without implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License v3 for more details; see <http://www.gnu.org/licenses/>.

from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

from footprint.client.configuration.default.built_form.default_croptype import RUCS_CROPTYPE_COLORS
from footprint.client.configuration.fixture import BuiltFormFixture, LandUseSymbologyFixture
from footprint.client.configuration.sacog.built_form.sacog_land_use_definition import SacogLandUseDefinition
from footprint.client.configuration.sacog.built_form.sacog_land_use import SacogLandUse
from footprint.main.lib.functions import merge
from footprint.main.models.config.region import Region
from footprint.main.models.built_form.urban.building_type import BuildingType
from footprint.main.models.built_form.urban.urban_placetype import UrbanPlacetype
from footprint.main.models.built_form.agriculture.crop_type import CropType
from footprint.main.utils.fixture_list import FixtureList
from django.conf import settings

class SacogBuiltFormFixture(BuiltFormFixture):
    def built_forms(self):
        return merge(
            self.parent_fixture.built_forms(client=settings.CLIENT),
            self.parent_fixture.built_forms(),
            dict(sacog_land_use=self.construct_client_land_uses(SacogLandUse, 'sac_lu')))

    def tag_built_forms(self, built_forms_dict):
        self.parent_fixture.tag_built_forms(built_forms_dict),

    def built_form_sets(self):
        return self.parent_fixture.built_form_sets() + FixtureList([
            dict(
                scope=Region,
                key='sacog_building_type',
                attribute='building_attribute_set',
                name='SACOG Buildingtypes',
                description='Built Forms for SACOG',
                client='sacog',
                clazz=BuildingType,
            ),
            dict(
                scope=Region,
                key='sacog_rucs',
                name='RUCS Types',
                attribute='agriculture_attribute_set',
                description='SACOG RUCS types',
                client=False,
                clazz=CropType,
            ),
        ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)
