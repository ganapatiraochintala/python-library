"""Python package for using the Urban Airship API"""
from .core import Airship
from .common import AirshipFailure, Unauthorized
from .push import (
    Push,
    ScheduledPush,
    ScheduledList,
    TemplatePush,
    Template,
    TemplateList,
    all_,
    ios_channel,
    android_channel,
    amazon_channel,
    channel,
    open_channel,
    device_token,
    apid,
    wns,
    tag,
    alias,
    segment,
    and_,
    or_,
    not_,
    location,
    recent_date,
    absolute_date,
    notification,
    ios,
    android,
    amazon,
    web,
    wns_payload,
    open_platform,
    message,
    in_app,
    device_types,
    options,
    campaigns,
    actions,
    interactive,
    wearable,
    public_notification,
    style,
    scheduled_time,
    local_scheduled_time,
    best_time,
    named_user,
    merge_data,
)

from .automation import (
    Automation,
    Pipeline
)

from .devices import (
    ChannelList,
    ChannelInfo,
    OpenChannel,
    DeviceTokenList,
    APIDList,
    DeviceInfo,
    TagList,
    Tag,
    DeleteTag,
    BatchTag,
    ChannelTags,
    OpenChannelTags,
    Segment,
    SegmentList,
    ChannelUninstall,
    NamedUser,
    NamedUserList,
    StaticList,
    StaticLists,
    LocationFinder,
)

from .reports import (
    IndividualResponseStats,
    ResponseList,
    DevicesReport,
    OptInList,
    OptOutList,
    PushList,
    ResponseReportList,
    AppOpensList,
    TimeInAppList,
)

__all__ = [
    Airship,
    AirshipFailure,
    Unauthorized,
    all_,
    Push,
    ScheduledPush,
    TemplatePush,
    ios_channel,
    android_channel,
    amazon_channel,
    channel,
    open_channel,
    device_token,
    apid,
    wns,
    tag,
    alias,
    segment,
    and_,
    or_,
    not_,
    location,
    recent_date,
    absolute_date,
    notification,
    ios,
    android,
    amazon,
    web,
    wns_payload,
    open_platform,
    message,
    in_app,
    options,
    campaigns,
    actions,
    interactive,
    device_types,
    scheduled_time,
    local_scheduled_time,
    ChannelList,
    ChannelInfo,
    OpenChannel,
    DeviceTokenList,
    APIDList,
    DeviceInfo,
    TagList,
    Tag,
    DeleteTag,
    BatchTag,
    Segment,
    SegmentList,
    ChannelUninstall,
    NamedUser,
    NamedUserList,
    IndividualResponseStats,
    ResponseList,
    DevicesReport,
    OptInList,
    OptOutList,
    PushList,
    ResponseReportList,
    AppOpensList,
    TimeInAppList,
    StaticList,
    StaticLists,
    LocationFinder,
    named_user,
    merge_data,
    Template,
    TemplateList,
    ScheduledList,
    Automation,
    Pipeline,
]

# Silence urllib3 INFO logging by default

import logging
logging.getLogger('requests.packages.urllib3.connectionpool')\
    .setLevel(logging.WARNING)
