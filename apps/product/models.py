# py
# django
from django.db import models
# drf
# third
from simple_history.models import HistoricalRecords
# own
from apps.core.models import BaseModels

# Create your models here.

class MeasureUnits(BaseModels):
    """Model definition for MeasureUnits."""

    # TODO: Define fields here.
    description = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for MeasureUnits."""

        verbose_name = 'MeasureUnit'
        verbose_name_plural = 'MeasureUnits'

    def __str__(self):
        """Unicode representation of MeasureUnits."""
        return self.description

class CategoriesProduct(BaseModels):
    """Model definition for CategoriesProduct."""

    # TODO: Define fields here
    description = models.CharField('Description', max_length=50, unique=True, blank=False, null=False)
    measure_unit = models.ForeignKey(MeasureUnits, on_delete=models.CASCADE, verbose_name='Measure Unit')
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for CategoriesProduct."""

        verbose_name = 'CategoriesProduct'
        verbose_name_plural = 'CategoriesProducts'

    def __str__(self):
        """Unicode representation of CategoriesProduct."""
        return self.description

class Indicators(BaseModels):
    """Model definition for Indicators."""

    # TODO: Define fields here
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoriesProduct, on_delete=models.CASCADE, verbose_name='Offer Indicator')
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Indicators."""

        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'

    def __str__(self):
        """Unicode representation of Indicators."""
        return f'Offer category: {self.category_product}, descount value: {self.descount_value}.'

class Products(BaseModels):
    """Model definition for Products."""
    
    # TODO: Define fields here
    name = models.CharField('Product Name', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Product Description', blank=False, null=False)
    image = models.ImageField('Product Image', upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Products."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Products."""
        return self.name