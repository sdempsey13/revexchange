from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Currency(models.Model):
    REV_TOKEN = 'REV'
    UNITED_STATES_DOLLAR = 'USD'
    ETHER = 'ETH'
    BITCOIN = 'BTC'
    USDT = 'USDT'
    CURRENCY_CHOICES = (
        (REV_TOKEN, 'REV'),
        (UNITED_STATES_DOLLAR, 'USD'),
        (ETHER, 'ETH'),
        (BITCOIN, 'BTC'),
        (USDT, 'USDT'),
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default=REV_TOKEN,
    )
    def __str__(self):
        return self.currency

class State(models.Model):
    state = models.CharField(max_length=50)
    def __str__(self):
        return self.state

class Trim(models.Model):
    trim = models.CharField(max_length=50)
    def __str__(self):
        return self.trim

class VModel(models.Model):
    vmodel = models.CharField(max_length=50)
    trim = models.ForeignKey(Trim, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        return self.vehicle_model

class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=50)
    vmodel = models.ForeignKey(VModel, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        return self.manufacturer

class Vehicle(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, blank=True, null=True)
    license_plate = models.CharField(max_length=7)
    vin = models.CharField(max_length=17)
    year = models.CharField(max_length=4)
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    num_doors = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    num_cylinders = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    ac_front = models.BooleanField()
    ac_rear = models.BooleanField()
    cruise_control = models.BooleanField()
    navigation = models.BooleanField()
    power_locks = models.BooleanField()
    power_steering = models.BooleanField()
    keyless_entry = models.BooleanField()
    integrated_phone = models.BooleanField()
    airbag_driver = models.BooleanField()
    airbag_passenger = models.BooleanField()
    arbag_side = models.BooleanField()
    antilock_brakes = models.BooleanField()
    fog_lights = models.BooleanField()
    rear_window_defrost = models.BooleanField()
    rear_window_wiper = models.BooleanField()
    tinted_glass = models.BooleanField()
    am_fm_stereo = models.BooleanField()
    cd_player = models.BooleanField()
    alloy_wheels = models.BooleanField()
    dvd_system = models.BooleanField()
    sun_roof = models.BooleanField()
    power_windows = models.BooleanField()
    premium_sound_system = models.BooleanField()
    security_alarm = models.BooleanField()
    third_row_seats = models.BooleanField()
    tow_package = models.BooleanField()
    CONVERTIBLE = 'CON'
    COUPE = 'COU'
    HATCHBACK = 'HAT'
    SEDAN = 'SED'
    SUV = 'SUV'
    BODY_STYLE_CHOICES = (
        (CONVERTIBLE, 'Convertible'),
        (COUPE, 'Coupe'),
        (HATCHBACK, 'Hatchback'),
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
    )
    body_style = models.CharField(
        max_length=3,
        choices=BODY_STYLE_CHOICES,
        default=COUPE,
    )
    STANDARD = 'S'
    PLATINUM = 'P'
    CENTURION = 'C'
    LISTING_PLAN_CHOICES = (
        (STANDARD, 'Standard'),
        (PLATINUM, 'Platinum'),
        (CENTURION, 'Centurion'),
    )
    listing_plan_choice = models.CharField(
        max_length=1,
        choices=LISTING_PLAN_CHOICES,
        default=CENTURION,
    )
    MANUAL = 'M'
    AUTOMATIC = 'A'
    CVT = 'C'
    TRANSMISSION_CHOICES = (
        (MANUAL, 'Manual'),
        (AUTOMATIC, 'Automattic'),
        (CVT, 'CVT'),
    )
    transmissions = models.CharField(
        max_length=1,
        choices=TRANSMISSION_CHOICES,
        default=AUTOMATIC,
    )
    BEIGETAN = 'BEI'
    BLACK = 'BLK'
    BLUE = 'BLU'
    BROWN = 'BRN'
    GOLD = 'GLD'
    GREY = 'GRY'
    GREEN = 'GRN'
    ORANGE = 'ORG'
    PINK = 'PNK'
    PURPLE = 'PPL'
    RED = 'RED'
    SILVER = 'SVR'
    WHITE = 'WHT'
    YELLOW = 'YLO'
    COLOR_CHOICES = (
        (BEIGETAN, 'Beige/Tan'),
        (BLACK, 'Black'),
        (BLUE, 'Blue'),
        (BROWN, 'Brown'),
        (GOLD, 'Gold'),
        (GREY, 'Grey'),
        (GREEN, 'Green'),
        (ORANGE, 'Orange'),
        (PINK, 'Pink'),
        (PURPLE, 'Purple'),
        (RED, 'Red'),
        (SILVER, 'Silver'),
        (WHITE, 'White'),
        (YELLOW, 'Yellow'),
    )
    interior_color = models.CharField(
        max_length=3,
        choices=COLOR_CHOICES,
        default=BLACK,
    )
    exterior_color = models.CharField(
        max_length=3,
        choices=COLOR_CHOICES,
        default=BLACK,
    )
    COMPRESSED_NATURAL_GAS = 'CNG'
    DIESEL = 'DIE'
    E85_FLEX_FUEL = 'E85'
    ELECTRIC = 'ELE'
    GASOLINE = 'GAS'
    HYBRID = 'HYB'
    FUEL_TYPE_CHOICES = (
        (COMPRESSED_NATURAL_GAS, 'Compressed Natural Gas'),
        (DIESEL, 'Diesel'),
        (E85_FLEX_FUEL, 'E85 Flex Fuel'),
        (ELECTRIC, 'Electric'),
        (GASOLINE, 'Gasoline'),
        (HYBRID, 'Hybrid'),
    )
    fueltypes = models.CharField(
        max_length=3,
        choices=FUEL_TYPE_CHOICES,
        default=GASOLINE,
    )
    TWO_WHEEL_DRIVE = '2'
    FOUR_WHEEL_DRIVE = '4'
    ALL_WHEEL_DRIVE = 'A'
    FRONT_WHEEL_DRIVE = 'F'
    REAR_WHEEL_DRIVE = 'R'
    DRIVE_TYPE_CHOICES = (
        (TWO_WHEEL_DRIVE, '2WD'),
        (FOUR_WHEEL_DRIVE, '4WD'),
        (ALL_WHEEL_DRIVE, 'AWD'),
        (FRONT_WHEEL_DRIVE, 'FWD'),
        (REAR_WHEEL_DRIVE, 'RWD'),
    )
    drivetypes = models.CharField(
        max_length=1,
        choices=DRIVE_TYPE_CHOICES,
        default=TWO_WHEEL_DRIVE,
    )
    image = models.FileField(null=True, blank=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    vehicle_history = models.URLField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.license_plate
