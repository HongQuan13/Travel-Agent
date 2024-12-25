export interface ItineraryCardProps {
  mainHeader: string;
  images: ImageCard[];
  subHeaders: object[];
}

export interface ImageCard {
  imageUrl: string;
}

export interface HeaderProps {
  title: string;
}

export interface PlaceCardHeaderProps {
  id: string;
  title: string;
  handleClick: (event: React.MouseEvent<HTMLDivElement>) => void;
}

export interface LocationCardProps {
  placeName: string;
  description: string;
  address: string;
  currentOpeningHours?: string;
  geometry?: string;
  internationalPhoneNumber?: string;
  reviews?: Review[];
  googleMapsUrl?: string;
  instagramUrl?: string;
  tiktokUrl?: string;

  // fix unmatch
  current_opening_hours?: string;
  international_phone_number?: string;
}

export interface ReviewsProps {
  reviews: Review[];
}

export interface Review {
  authorName: string;
  text: string;
  rating: number;
  relativeTimeDescription: string;

  // fix unmatch
  author_name?: string;
  relative_time_description?: string;
}
