from models import Property, ListingType, PropertyType, FurnishingStatus, search_properties

if __name__ == "__main__":
    # This block runs only when you do: python your_file.py
    # It won't run if another file imports from this one

    # Make some fake properties
    props = [
        Property(
            id=1,
            title="2BHK near Gandhipuram",
            description="Spacious apartment with parking",
            price=4500000,
            bedrooms=2,
            area_sqft=1100,
            city="Coimbatore",
            locality="Gandhipuram",
            listing_type=ListingType.SALE,
            property_type=PropertyType.APARTMENT,
            furnishing=FurnishingStatus.SEMI_FURNISHED,
        ),
        Property(
            id=2,
            title="3BHK Villa RS Puram",
            description="Gated community villa",
            price=12000000,
            bedrooms=3,
            area_sqft=2200,
            city="Coimbatore",
            locality="RS Puram",
            listing_type=ListingType.SALE,
            property_type=PropertyType.VILLA,
            furnishing=FurnishingStatus.FURNISHED,
            is_featured=True,
        ),
        Property(
            id=3,
            title="1BHK PG near PSG Tech",
            description="PG hostel for students",
            price=8000,
            bedrooms=1,
            area_sqft=400,
            city="Coimbatore",
            locality="Peelamedu",
            listing_type=ListingType.RENT,
            property_type=PropertyType.PG_HOSTEL,
            furnishing=FurnishingStatus.FURNISHED,
        ),
        Property(
            id=4,
            title="1BHK PG near PSG Tech",
            description="PG hostel for students",
            price=12000,
            bedrooms=1,
            area_sqft=700,
            city="Coimbatore",
            locality="Metupalayam",
            listing_type=ListingType.RENT,
            property_type=PropertyType.PG_HOSTEL,
            furnishing=FurnishingStatus.FURNISHED,
        ),
        Property(
            id=5,
            title="1BHK PG near PSG Tech",
            description="PG hostel for students",
            price=8000000,
            bedrooms=1,
            area_sqft=4000,
            city="Coimbatore",
            locality="Annur",
            listing_type=ListingType.SALE,
            property_type=PropertyType.INDEPENDENT_HOUSE,
            furnishing=FurnishingStatus.UNFURNISHED,
        ),
    ]

    print("--- All properties ---")
    for p in search_properties(props):
        print(f"  {p.title} - ₹{p.price}")

    print("--- Type Hostel ---")
    for p in search_properties(props, property_type=PropertyType.INDEPENDENT_HOUSE):
        print(f"  {p.title} - ₹{p.price}")

    print("--- Type max price 10000 ---")
    for p in search_properties(props, max_price=10000):
        print(f"  {p.title} - ₹{p.price}")

    print("--- Locality Annur ---")
    for p in search_properties(props, locality="Annur"):
        print(f"  {p.title} - ₹{p.price}")

    print("--- Furnished ---")
    for p in search_properties(props, furnishing=FurnishingStatus.FURNISHED):
        print(f"  {p.title} - ₹{p.price}")

    print("--- BHK ---")
    for p in search_properties(props, keywords=["1BHK"]):
        print(f"  {p.title} - ₹{p.price}")

    print("--- Listing Type ---")
    for p in search_properties(props, listing_type=ListingType.RENT):
        print(f"  {p.title} - ₹{p.price}")