interface MainHeaderProps {
  title: string;
}

export function MainHeader({ title }: MainHeaderProps) {
  return <h1 className="text-4xl font-bold tracking-tight mb-8">{title}</h1>;
}

interface SubHeaderProps {
  title: string;
}

export function SubHeader({ title }: SubHeaderProps) {
  return <h2 className="text-2xl font-semibold text-primary mb-6">{title}</h2>;
}
