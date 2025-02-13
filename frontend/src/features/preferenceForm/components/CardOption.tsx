import {
  Palmtree,
  LandmarkIcon,
  Mountain,
  Music,
  UtensilsCrossed,
  Moon,
  ShoppingBag,
  SpadeIcon as Spa,
  UserIcon,
  Users,
  UserPlus,
  UsersRound,
} from "lucide-react";

export const ACTIVITIES = [
  {
    value: "beaches",
    label: "Beaches",
    icon: <Palmtree className="h-8 w-8" />,
  },
  {
    value: "city",
    label: "City sightseeing",
    icon: <LandmarkIcon className="h-8 w-8" />,
  },
  {
    value: "outdoor",
    label: "Outdoor adventures",
    icon: <Mountain className="h-8 w-8" />,
  },
  {
    value: "festivals",
    label: "Festivals/events",
    icon: <Music className="h-8 w-8" />,
  },
  {
    value: "food",
    label: "Food exploration",
    icon: <UtensilsCrossed className="h-8 w-8" />,
  },
  {
    value: "nightlife",
    label: "Nightlife",
    icon: <Moon className="h-8 w-8" />,
  },
  {
    value: "shopping",
    label: "Shopping",
    icon: <ShoppingBag className="h-8 w-8" />,
  },
  { value: "spa", label: "Spa wellness", icon: <Spa className="h-8 w-8" /> },
];

export const COMPANIONS = [
  { value: "solo", label: "Solo", icon: <UserIcon className="h-8 w-8" /> },
  { value: "couple", label: "Couple", icon: <Users className="h-8 w-8" /> },
  { value: "family", label: "Family", icon: <UserPlus className="h-8 w-8" /> },
  {
    value: "friends",
    label: "Friends",
    icon: <UsersRound className="h-8 w-8" />,
  },
];

export const BUDGETS = [
  { value: "low", label: "Low", range: "0 - 1000 USD" },
  {
    value: "medium",
    label: "Medium",
    range: "1000 - 2500 USD",
  },
  { value: "high", label: "High", range: "2500+ USD" },
];
