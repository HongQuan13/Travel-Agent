import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { HashLoader } from "react-spinners";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import { createConversation } from "@/features/message";
import { Button } from "@/components/ui/button";
import { Form } from "@/components/ui/form";
import {
  ACTIVITIES,
  BUDGETS,
  COMPANIONS,
} from "@/features/preferenceForm/components/CardOption";
import { InputField } from "@/features/preferenceForm/components/InputField";
import {
  formSchema,
  TravelFormValues,
} from "@/features/preferenceForm/interfaces";
import { DatePickerField } from "@/features/preferenceForm/components/DatePickerField";
import { CardSelectionField } from "@/features/preferenceForm/components/CardSelectionField";

export default function Home() {
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const form = useForm<TravelFormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      destination: "",
      dayDuration: 1,
      budget: "",
      travelCompanion: "",
      activities: [],
    },
  });

  const onSubmit = async (data: TravelFormValues) => {
    console.log("Form submitted:", data);
    try {
      setLoading(true);
      const newConversation = await createConversation(data);
      const conversationId = newConversation.conversationId;
      navigate(`/chatbot?conversationId=${conversationId}`);
    } catch (error) {
      console.log("handle send message error", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-8">
        Tell us your travel preferences
      </h1>

      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
          {/* Destination */}
          <InputField
            control={form.control}
            name="destination"
            label="What is your destination of choice?"
            placeholder="Enter your desired destination"
            type={""}
          />

          {/* Travel Date */}
          <DatePickerField
            control={form.control}
            name="travelDate"
            label="When are you planning to travel?"
          />

          {/* Duration */}
          <InputField
            control={form.control}
            name="dayDuration"
            label="How many days are you planning to travel?"
            type="number"
            placeholder="Enter number of days"
          />

          {/* Budget */}
          <CardSelectionField
            form={form}
            name="budget"
            label="What is your budget?"
            options={BUDGETS}
          />

          {/* Travel Companions */}
          <CardSelectionField
            form={form}
            name="travelCompanion"
            label="Who do you plan on traveling with?"
            options={COMPANIONS}
          />

          {/* Activities */}
          <CardSelectionField
            form={form}
            name="activities"
            label="Which activities are you interested in?"
            options={ACTIVITIES}
            multiple
          />

          <Button type="submit" className="w-full">
            Submit Preferences
            {loading ? <HashLoader size={30} color="white" /> : <></>}
          </Button>
        </form>
      </Form>
    </div>
  );
}
