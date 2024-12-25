export interface ItineraryCardProps {
  mainHeader: string;
  images: ImageCard[];
  subHeaders: object[];
}

export interface ImageCard {
  image_url: string;
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
  current_opening_hours?: string;
  geometry?: string;
  international_phone_number?: string;
  reviews?: Review[];
  googleMapsUrl?: string;
  instagramUrl?: string;
  tiktokUrl?: string;
}

export interface ReviewsProps {
  reviews: Review[];
}

export interface Review {
  author_name: string;
  text: string;
  rating: number;
  relative_time_description: string;
}
