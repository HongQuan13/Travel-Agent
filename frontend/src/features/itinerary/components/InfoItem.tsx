import { LocationCardProps } from "../interfaces";
import { Reviews } from "./ReviewCard";

export const InfoItem = ({ placeInfo }: { placeInfo: LocationCardProps }) => {
  const infoList = [
    { label: "Address", value: placeInfo.address },
    { label: "Opening Hours", value: placeInfo.current_opening_hours },
    { label: "Phone Number", value: placeInfo.international_phone_number },
  ];
  return (
    <div>
      {infoList.map(
        (item, index) =>
          item.value && (
            <div key={index} className="flex items-center space-x-2 mb-1">
              <h4 className="font-semibold">{item.label}:</h4>
              <p className="text-sm text-muted-foreground">{item.value}</p>
            </div>
          )
      )}

      {placeInfo.reviews && placeInfo.reviews[0].text && (
        <Reviews reviews={placeInfo.reviews} />
      )}
    </div>
  );
};
