from django.utils.translation import ugettext_lazy as _

RESOURCE_PERMISSIONS = (
    ('can_approve_reservation', _('Can approve reservation')),
    ('can_make_reservations', _('Can make reservations')),
    ('can_modify_reservations', _('Can modify reservations')),
    ('can_ignore_opening_hours', _('Can make reservations outside opening hours')),
    ('can_view_reservation_access_code', _('Can view reservation access code')),
    ('can_view_reservation_extra_fields', _('Can view reservation extra fields')),
    ('can_view_reservation_user', _('Can view reservation user')),
    ('can_access_reservation_comments', _('Can access reservation comments')),
    ('can_comment_reservations', _('Can create comments for a reservation')),
    ('can_view_reservation_catering_orders', _('Can view reservation catering orders')),
    ('can_modify_reservation_catering_orders', _('Can modify reservation catering orders')),
    ('can_view_reservation_product_orders', _('Can view reservation product orders')),
    ('can_modify_paid_reservations', _('Can modify paid reservations')),
    ('can_bypass_payment', _('Can bypass payment for paid reservations')),
)

UNIT_PERMISSIONS = [
    ('unit:' + name, description)
    for (name, description) in RESOURCE_PERMISSIONS
]

RESOURCE_GROUP_PERMISSIONS = [
    ('group:' + name, description)
    for (name, description) in RESOURCE_PERMISSIONS
]
