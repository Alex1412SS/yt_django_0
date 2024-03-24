/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./bluepage/**/*.{html,js}"],
  theme: {
    extend: {
     padding: {
        bigPadd: '50px',
        noBig:'5px',
        verybig:'150px'
      },
      width:{
        image: '525px',
        twxt: '500px',
        svgg: '150px',
        reasd: '300px',
        maxais: '1200px'
      },
      height: {
        heidf: '85px',
        back:'250px'
      },
      },
  },
  plugins: [],
}

