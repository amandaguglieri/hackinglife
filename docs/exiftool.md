---
title: exiftool - A tool for metadata edition
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
---

# exiftool - A tool for metadata edition


```
exiftool -common dir
            Print common meta information for all images in "dir".  "-common" is a shortcut tag representing
            common EXIF meta information.

       exiftool -T -createdate -aperture -shutterspeed -iso dir > out.txt
            List specified meta information in tab-delimited column form for all images in "dir" to an output
            text file named "out.txt".

       exiftool -s -ImageSize -ExposureTime b.jpg
            Print ImageSize and ExposureTime tag names and values.

       exiftool -l -canon c.jpg d.jpg
            Print standard Canon information from two image files.

       exiftool -r -w .txt -common pictures
            Recursively extract common meta information from files in "pictures" directory, writing text output
            to ".txt" files with the same names.

       exiftool -b -ThumbnailImage image.jpg > thumbnail.jpg
            Save thumbnail image from "image.jpg" to a file called "thumbnail.jpg".

       exiftool -b -JpgFromRaw -w _JFR.JPG -ext NEF -r .
            Recursively extract JPG image from all Nikon NEF files in the current directory, adding "_JFR.JPG"
            for the name of the output JPG files.

       exiftool -a -b -W %d%f_%t%-c.%s -preview:all dir
            Extract all types of preview images (ThumbnailImage, PreviewImage, JpgFromRaw, etc.) from files in
            directory "dir", adding the tag name to the output preview image file names.

       exiftool -d '%r %a, %B %e, %Y' -DateTimeOriginal -S -s -ext jpg .
            Print formatted date/time for all JPG files in the current directory.

       exiftool -IFD1:XResolution -IFD1:YResolution image.jpg
            Extract image resolution from EXIF IFD1 information (thumbnail image IFD).

       exiftool '-*resolution*' image.jpg
            Extract all tags with names containing the word "Resolution" from an image.

       exiftool -xmp:author:all -a image.jpg
            Extract all author-related XMP information from an image.

       exiftool -xmp -b a.jpg > out.xmp
        Extract complete XMP data record intact from "a.jpg" and write it to "out.xmp" using the special
            "XMP" tag (see the Extra tags in Image::ExifTool::TagNames).

```

