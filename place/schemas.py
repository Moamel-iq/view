from ninja import Schema
from pydantic import UUID4
from typing import List, Optional
from pydantic import HttpUrl
from ninja import UploadedFile
from account.schemas import AccountOut
from location.schemas import CityOut, CountryOut
from place.models import PlaceMixin, Company


class SocialMediaSchema(Schema):
    facebook: str = None
    instagram: str = None
    telegram: str = None
    whatsapp: str = None
    is_available: List[str] = None




class PlaceImageOut(Schema):
    id: UUID4
    image: str
    image_url: HttpUrl = None


class PlaceMixinOut(Schema):
    id: UUID4
    name: str
    # location: str
    city: CityOut
    longitude: float
    latitude: float
    description: str
    short_location: str
    price: Optional[float]
    place_images: List[PlaceImageOut]
    social_media: Optional[SocialMediaSchema]
    place_type: str
    type: str = None
    average_rating: Optional[float]
    review_count: Optional[int]
    open: Optional[str]
    phone_number: Optional[str]

    class Config:
        orm_mode = True

    @staticmethod
    def from_orm(place: PlaceMixin):
        is_available = place.get_social_media

        user = place.user.is_merchant if place.user else None
        return PlaceMixinOut(
            id=place.id,
            name=place.name,
            city=CityOut.from_orm(place.city),
            longitude=place.longitude,
            latitude=place.latitude,
            description=place.description,
            short_location=place.short_location,
            place_images=[PlaceImageOut.from_orm(image) for image in place.place_images],
            average_rating=place.average_rating,
            review_count=place.review_count,
            social_media=is_available,
            place_type=place.get_place_type,
            type=place.get_place_sub_type or None,
            price=place.price,
            open=place.open,
            user=user,
            phone_number=place.phone_number,
        )


class PlaceMixinSchema(Schema):
    total_count: int = None
    per_page: int = None
    from_record: int = None
    to_record: int = None
    previous_page: int = None
    next_page: int = None
    current_page: int = None
    page_count: int = None
    data: List[PlaceMixinOut]


class ReviewSchema(Schema):
    id: UUID4
    user:AccountOut
    place_id: UUID4 = None
    company_id: UUID4 = None
    entity_type: str
    comment: str
    rating: int


class ReviewsIn(Schema):
    comment: Optional[str]
    rating: int



class AdvertisementSchema(Schema):
    id: UUID4
    country: CountryOut = None
    image: str
    title: str
    short_description: str
    url: str = None
    place: PlaceMixinOut = None


class OfferSchema(Schema):
    id: UUID4
    country: CountryOut
    image: str
    url: str = None
    place: PlaceMixinOut = None


class RecommendedPlacesOut(Schema):
    id: UUID4
    country: CountryOut
    place: PlaceMixinOut


class LatestPlacesOut(Schema):
    id: UUID4
    country: CountryOut
    place: PlaceMixinOut


class LatestPlacesCity(Schema):
    id: UUID4
    city: CityOut
    place: PlaceMixinOut


class FavoritePlaceOut(Schema):
    id: UUID4
    place: PlaceMixinOut


class CompanyOut(Schema):
    id: UUID4
    city: CityOut
    company_name: str
    image: str = None
    company_description: str
    longitude: float
    latitude: float
    social_media: Optional[SocialMediaSchema]
    average_rating: Optional[float]
    review_count: Optional[int]

    @staticmethod
    def from_orm(company: Company):
        def social_media():
            SOCIAL_MEDIA_APPS = {
                'facebook': 'facebook',
                'instagram': 'instagram',
                'telegram': 'telegram',
                'whatsapp': 'whatsapp',
            }

            facebook = company.social_media_company.values_list('facebook', flat=True)
            instagram = company.social_media_company.values_list('instagram', flat=True)
            telegram = company.social_media_company.values_list('telegram', flat=True)
            whatsapp = company.social_media_company.values_list('whatsapp', flat=True)
            is_available = {
                'facebook': facebook if facebook else None,
                'instagram': instagram if instagram else None,
                'telegram': telegram if telegram else None,
                'whatsapp': whatsapp if whatsapp else None,
            }
            return facebook


        return CompanyOut(
            id=company.id,
            city=CityOut.from_orm(company.city),
            company_name=company.company_name,
            image=company.image_url,
            company_description=company.company_description,
            longitude=company.longitude,
            latitude=company.latitude,
            social_media=social_media,
            average_rating=company.average_rating,
            review_count=company.review_count,
        )

class TripDetailOut(Schema):
    id: UUID4
    trip_name: str
    short_description: str
    trip_details: str
    trip_images: List[PlaceImageOut] = None


class CompanyWithTripsOut(Schema):
    company: CompanyOut
    trip_details: List[TripDetailOut]


class PlaceCreate(Schema):
    user_id: UUID4
    name: str
    city_id: UUID4
    location: str
    short_location: str = None
    description: str = None
    price: float = None
    place_type: str
    type: str = None
    open: str = None
    phone_number: str = None
    facebook: str = None
    instagram: str = None
    telegram: str = None
    whatsapp: str = None


class PlaceUpdate(Schema):
    name: str = None
    description: str = None
    price: float = None
    open: str = None
    phone_number: int = None
    facebook: str = None
    instagram: str = None
    telegram: str = None
    whatsapp: str = None

