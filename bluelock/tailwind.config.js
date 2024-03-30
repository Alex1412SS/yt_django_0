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
        back:'250px',
        imagehei: '160px',
        blockmge: '200px'
      },
      backgroundImage: {
        'footer-texture':"url('https://img.freepik.com/free-photo/liquid-marbling-paint-texture-background-fluid-painting-abstract-texture-intensive-color-mix-wallpaper_1258-100248.jpg?w=1060&t=st=1710493482~exp=1710494082~hmac=cfe5198df99fec906c8a8f45a15a34d028271dbf6e1ed18472467b2f19f93e9f')"
      },
      margin: {
      fefcas:'250px'
      }
      },
  },
  plugins: [],
}

