from odoo import models, fields


class PartnerMixin(models.AbstractModel):
    """
    Nouvelle classe abstraite qui va être utilisée comme mixin pour afficher
    les champs related des partenaires.
    """

    _name = "partner.mixin"
    _description = "Partner Mixin"

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Client",
        required=True,
        tracking=True,
    )
    company_type = fields.Selection(
        related="partner_id.company_type",
        string="Type",
        readonly=False,
        tracking=True,
    )
    title = fields.Many2one(
        related="partner_id.title",
        string="Civilité",
        readonly=False,
        required=True,
        tracking=True,
    )
    lastname = fields.Char(
        related="partner_id.lastname",
        string="Nom de famille",
        readonly=False,
        tracking=True,
    )
    firstname = fields.Char(
        related="partner_id.firstname",
        string="Prénom",
        readonly=False,
        tracking=True,
    )
    phone = fields.Char(
        related="partner_id.phone",
        string="Téléphone 1",
        readonly=False,
        tracking=True,
        required=True,
    )
    phone_2 = fields.Char(
        related="partner_id.phone_2",
        string="Téléphone 2",
        readonly=False,
        tracking=True,
    )
    phone_3 = fields.Char(
        related="partner_id.phone_3",
        string="Téléphone 3",
        readonly=False,
        tracking=True,
    )
    email = fields.Char(
        related="partner_id.email",
        string="Email",
        readonly=False,
        tracking=True,
    )
    mail_2 = fields.Char(
        related="partner_id.mail_2",
        string="Email 2",
        readonly=False,
        tracking=True,
    )
    floor = fields.Char(
        related="partner_id.floor",
        string="Etage",
        readonly=False,
        tracking=True,
    )
    building = fields.Char(
        related="partner_id.building",
        string="Bâtiment",
        readonly=False,
        tracking=True,
    )
    code = fields.Char(
        related="partner_id.code", string="Code", readonly=False, tracking=True
    )
    street = fields.Char(
        related="partner_id.street",
        string="Adresse",
        readonly=False,
        required=True,
        tracking=True,
    )
    city = fields.Char(
        related="partner_id.city",
        string="Ville",
        readonly=False,
        required=True,
        tracking=True,
    )
    zip = fields.Char(
        related="partner_id.zip",
        string="Code postal",
        readonly=False,
        required=True,
        tracking=True,
    )
    street_number = fields.Char(
        related="partner_id.street_number",
        string="Numéro",
        readonly=False,
        required=True,
        tracking=True,
    )
    limit_geo_distance = fields.Integer(
        related="partner_id.limit_geo_distance",
        string="Limite Géo. Rayon",
        readonly=False,
        tracking=True,
    )
    company_name = fields.Char(
        related="partner_id.company_name",
        string="Société",
        readonly=False,
        tracking=True,
    )
    sh_contact_google_location = fields.Char(
        string="Adresse"
    )

    city_zip = fields.Char(
        string="Ville, Code Postal",
        compute="_compute_city_zip",
        store=True,
    )
    test = fields.Boolean(
        default=True,
        string="test booleen"
    )

    def _compute_city_zip(self):
        """
        Concaténer le code postal et la ville pour former la ville, code postal.
        """
        for record in self:
            if record.city and record.zip:
                record.city_zip = f"{record.city} {record.zip}"
            elif record.city: 
                record.city_zip = record.city
            elif record.zip: 
                record.city_zip = record.zip
            else:
                record.city_zip = ""
