import PyPDF2
import pyttsx3


class Reading:
    book = open('E:\\Bhagavad-gita_As_It_Is.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    paged = pdfReader.numPages
    print(paged)
    speak = pyttsx3.init()
    from_page = pdfReader.getPage(12)
    text = from_page.extractText()
    speak.say(text)
    speak.runAndWait()


