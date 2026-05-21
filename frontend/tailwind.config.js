/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        blue: {
          DEFAULT: '#0F4C81',
          mid: '#1B6CA8',
          light: '#D6E8F7',
        },
        amber: {
          DEFAULT: '#F5A623',
          dark: '#D4881A',
          light: '#FEF3DC',
        },
        ink: {
          DEFAULT: '#1A2535',
          soft: '#2E4260',
          muted: '#6B82A0',
        },
        canvas: {
          DEFAULT: '#F4F7FA',
          alt: '#E8EEF5',
        },
        green: {
          DEFAULT: '#1A7A52',
          light: '#E8F5EC',
        },
        dark: {
          bg: '#0A1628',
        },
      },
      fontFamily: {
        display: ['Syne', 'sans-serif'],
        body: ['DM Sans', 'sans-serif'],
        serif: ['Playfair Display', 'serif'],
      },
      borderRadius: {
        'sm': '6px',
        'md': '12px',
        'lg': '20px',
        'xl': '32px',
      },
      boxShadow: {
        'sm': '0 2px 8px rgba(15,76,129,.08)',
        'md': '0 6px 24px rgba(15,76,129,.14)',
        'lg': '0 16px 48px rgba(15,76,129,.18)',
      },
    },
  },
  plugins: [],
}
