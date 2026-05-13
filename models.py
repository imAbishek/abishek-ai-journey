from dataclasses import dataclass
from enum import Enum


class ListingType(Enum):
    SALE = "sale"
    RENT = "rent"
    PG = "pg"

class PropertyType(Enum):
    APARTMENT = "apartment"
    INDEPENDENT_HOUSE = "independent_house"
    VILLA ="villa"
    PLOT = "plot"
    PG_HOSTEL = "pg_hostel"
    BUILDING_FLOOR = "building_floor"

class FurnishingStatus(Enum):
    FURNISHED = "furnished"
    SEMI_FURNISHED = "semi_furnished"
    UNFURNISHED = "unfurnished"

@dataclass
class Property:
    id: int
    title: str
    description: str
    price: float
    bedrooms: int
    area_sqft: float
    city: str
    locality: str
    listing_type: ListingType
    property_type: PropertyType
    furnishing: FurnishingStatus
    is_featured: bool = False

def search_properties(
        all_properties: list[Property],
        property_type: PropertyType | None = None,
        listing_type: ListingType | None = None,
        city: str | None = None,
        locality: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        min_bedrooms: int | None = None,
        max_bedrooms: int | None = None,
        min_area : float | None = None,
        max_area : float | None = None,
        furnishing: FurnishingStatus | None = None,
        featured: bool = False,
        keywords: list[str] | None = None,
) -> list[Property]:

    results = all_properties

    if property_type is not None:
        results = [p for p in results if p.property_type == property_type]

    if listing_type is not None:
        results = [p for p in results if p.listing_type == listing_type]

    if city is not None:
        results = [p for p in results if p.city == city]

    if locality is not None:
        results = [p for p in results if p.locality == locality]

    if min_price is not None:
        results = [p for p in results if p.price >= min_price]

    if max_price is not None:
        results = [p for p in results if p.price <= max_price]

    if min_bedrooms is not None:
        results = [p for p in results if p.bedrooms >= min_bedrooms]

    if max_bedrooms is not None:
        results = [p for p in results if p.bedrooms <= max_bedrooms]

    if min_area is not None:
        results = [p for p in results if p.area_sqft >= min_area]

    if max_area is not None:
        results = [p for p in results if p.area_sqft <= max_area]

    if furnishing is not None:
        results = [p for p in results if p.furnishing == furnishing]

    if featured:
        results = [p for p in results if p.is_featured]

    if keywords is not None:
        results = [p for p in results
               for kw in keywords
               if kw.lower() in p.title.lower() or kw.lower() in p.description.lower()]

    return results

