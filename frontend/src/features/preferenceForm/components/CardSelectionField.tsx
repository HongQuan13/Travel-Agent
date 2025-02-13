import { Card, CardContent } from "@/components/ui/card";
import { cn } from "@/lib/utils";
import {
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { CardFieldProps } from "../interfaces";

export const CardSelectionField = ({
  form,
  name,
  label,
  options,
  multiple = false,
}: CardFieldProps) => (
  <FormField
    control={form.control}
    name={name}
    render={({ field }) => (
      <FormItem className="space-y-4">
        <FormLabel>{label}</FormLabel>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {options.map((option) => (
            <Card
              key={option.value}
              className={cn(
                "cursor-pointer transition-colors",
                field.value?.includes(option.value) ||
                  field.value == option.value
                  ? "border-primary bg-primary/10"
                  : "hover:bg-muted/50"
              )}
              onClick={() => {
                if (multiple) {
                  // Handle multi-select (e.g., activities)
                  const newValues = field.value.includes(option.value)
                    ? field.value.filter((v: string) => v !== option.value)
                    : [...field.value, option.value];
                  form.setValue(name, newValues);
                } else {
                  // Handle single-select (e.g., budget, companion)
                  form.setValue(name, option.value);
                }
              }}
            >
              <CardContent className="p-4 text-center space-y-2">
                {option.icon && (
                  <div className="flex justify-center items-center h-12">
                    {option.icon}
                  </div>
                )}
                <div className="font-medium">{option.label}</div>
                {option.range && (
                  <div className="text-sm text-muted-foreground">
                    {option.range}
                  </div>
                )}
              </CardContent>
            </Card>
          ))}
        </div>
        <FormMessage />
      </FormItem>
    )}
  />
);
