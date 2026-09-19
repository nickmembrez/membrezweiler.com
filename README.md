# membrezweiler.com

A static personal academic site. No build step, no framework, no dependencies to install. Every page is plain HTML, one shared stylesheet, and one small script.

## Getting it online

Upload the entire contents of this folder to your host so that `index.html` sits at the domain root. Three options, easiest first.

**Cloudflare Pages or Netlify (free, recommended).** Create an account, choose the option to deploy without a git repository, and drag this whole folder onto the upload area. Then add `membrezweiler.com` as a custom domain and follow the DNS instructions the host gives you. Updating the site later means dragging the folder again.

**Your registrar's own hosting.** If whoever you registered the domain through offers hosting, use their file manager or an FTP client and upload the contents of this folder into the public web directory, which is usually called `public_html` or `www`. Upload the contents, not the folder itself.

**GitHub Pages.** Create a repository, upload these files to the root of the default branch, turn on Pages in the repository settings, and add the custom domain there.

Whichever you pick, confirm afterward that `https://membrezweiler.com/labs/WCC_Lab01_WhoCounts.html` loads, which tells you the `labs` subfolder came across intact.

## What is in here

```
index.html                 Home
research.html              Research narrative, publications, in progress, future plans, dissertation
teaching.html              Teaching approach and all courses grouped by area
teaching-resources.html    The lab repository, searchable and filterable
students.html              Advising, research opportunities, letters of recommendation
service.html               Reviewing, association and departmental service, invited talks
cv.html                    Web version of the CV plus the download
404.html                   Not-found page
robots.txt, sitemap.xml    Search engine basics
assets/css/site.css        The entire design system
assets/js/site.js          Theme toggle and lab filtering
assets/img/                Portrait, social share card, favicon
assets/cv/                 CV in PDF and Word
labs/                      The 47 lab pages, unmodified
```

## Making changes

**Text.** Open the relevant `.html` file in any text editor and edit between the tags. Nothing needs to be rebuilt.

**A new publication.** Copy an existing `<li class="entry">` block in `research.html` and in `cv.html`, then change the year, title, citation, and DOI.

**A new lab.** Drop the HTML file into `labs/`, then add one entry to the `LABS` list in `build_resources.py` (kept alongside this folder) and run `python3 build_resources.py`, or copy an existing `<li class="lab">` block in `teaching-resources.html` by hand. Update the counts on `index.html` and `teaching.html` if you want them exact.

**A new CV.** Replace `assets/cv/Membrez-Weiler_CV.pdf` and `.docx` with the new files, keeping the same filenames so the download link keeps working, and update `cv.html` to match.

**Colors and type.** Everything is defined as custom properties at the top of `assets/css/site.css`, in a light block and a dark block. Change a value once and it applies everywhere.

## Things to check before you publish

A few items came from sources that disagreed, or that I could not confirm. Worth a look.

1. **Distinct course count.** The teaching page says seventeen distinct courses, counted by unique course title across all five institutions. If you would rather count course listings, the number is twenty-three.

2. **Dissertation link.** The research page mentions the NC State ETD collection without linking to it, because I could not verify a stable URL. Paste the real link in when you have it.

3. **White-collar crime course number.** The Spring 2027 white-collar crime course is listed without a number on `cv.html` and `teaching.html`, since the department had not assigned one. Add it when you have it.

4. **The gambling paper in progress.** I described the legal-avoidance paper from your design memo. Check that the description matches where the paper actually landed, and that your coauthors are comfortable with it being listed publicly.

5. **Lab pages reference D2L.** Several labs tell students to paste their answers into a D2L submission. That reads fine to another instructor, but if you would rather the public copies say something generic, the phrase to search for is "in D2L".

6. **Job market line.** I deliberately did not put anything on the site about looking for a position. If you want a line like that, the natural place is just under the title on the home page, and I can add it.

## Optional additions

Things the structure already supports if you want them later: a public writing or media page, a contact form (which needs a third-party service such as Formspree, since static hosting cannot send mail), a Google Scholar link next to ORCID once you have a profile, and PDF preprints of the working papers linked from the research page.
