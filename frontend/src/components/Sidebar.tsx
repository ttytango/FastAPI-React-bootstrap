export default function Sidebar() {
  const items = [
    { label: 'Status', href: '#' },
    { label: 'Create User', href: '#' },
    { label: 'Login', href: '#' },
    { label: 'Me', href: '#' },
    { label: 'Settings', href: '#' },
  ]

  return (
    <aside className="hidden md:flex md:flex-col md:w-56 bg-white border-r border-gray-200 min-h-[calc(100vh-64px)] sticky top-16">
      <div className="p-4 text-sm font-semibold text-gray-500">Navigation</div>
      <nav className="px-2 pb-4 space-y-1">
        {items.map((it) => (
          <a key={it.label} href={it.href} className="flex items-center gap-3 px-3 py-2 rounded-md text-gray-700 hover:bg-gray-50">
            <span className="h-2 w-2 rounded-full bg-gray-300" />
            <span className="text-sm font-medium">{it.label}</span>
          </a>
        ))}
      </nav>
      <div className="mt-auto p-4 text-xs text-gray-400">v0.1</div>
    </aside>
  )
}


