interface HeaderProps {
  title: string;
}

export function MainHeader({ title }: HeaderProps) {
  return <h1 className="text-4xl font-bold tracking-tight mb-8">{title}</h1>;
}

export function SubHeader({ title }: HeaderProps) {
  return <h2 className="text-2xl font-semibold text-primary mb-6">{title}</h2>;
}
