const googleTTS = require('google-tts-api');

// Text you want to convert to speech
const text = 'Hello, welcome to the Voice from Text project.';

// Get the audio URL for the given text
const url = googleTTS.getAudioUrl(text, {
  lang: 'en',
  slow: false,
  host: 'https://translate.google.com',
});

// Log the URL where you can access the audio
console.log(url);
