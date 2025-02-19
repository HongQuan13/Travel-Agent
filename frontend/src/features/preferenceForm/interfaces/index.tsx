import * as z from "zod";

export const formSchema = z.object({
  destination: z.string().min(1, "Destination is required"),
  travelDate: z.date({
    required_error: "Please select a travel date",
  }),
  dayDuration: z.coerce.number().int().min(1, "Duration is required").max(10),
  budget: z.string().min(1, "Please select a budget range"),
  travelCompanion: z.string().min(1, "Please select who you're traveling with"),
  activities: z.array(z.string()).min(1, "Please select at least one activity"),
});

export type TravelFormValues = z.infer<typeof formSchema>;

export type Option = {
  value: string;
  label: string;
  range?: string;
  icon?: React.ReactNode;
};

export interface InputFieldProps {
  control: any;
  name: keyof TravelFormValues;
  label: string;
  type: string;
  placeholder: string;
}

export interface DateFieldProps {
  control: any;
  name: keyof TravelFormValues;
  label: string;
}

export interface CardFieldProps {
  form: any;
  name: keyof TravelFormValues;
  label: string;
  options: Option[];
  multiple?: boolean;
}
