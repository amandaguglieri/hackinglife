---
title: exiftool - A tool for metadata edition
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - file
---

# exiftool - A tool for metadata edition

ExifTool is a platform-independent Perl library plus a command-line application for reading, writing and editing meta information in a wide variety of files. ExifTool supports many different metadata formats including EXIF, GPS, IPTC, XMP, JFIF, GeoTIFF, ICC Profile, Photoshop IRB, FlashPix, AFCP and ID3, Lyrics3, as well as the maker notes of many digital cameras by Canon, Casio, DJI, FLIR, FujiFilm, GE, GoPro, HP, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Motorola, Nikon, Nintendo, Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Phase One, Reconyx, Ricoh, Samsung, Sanyo, Sigma/Foveon and Sony.

ExifTool can **R**ead, **W**rite and/or **C**reate files in the following formats. Also listed are the support levels for EXIF, IPTC (IIM), XMP, ICC_Profile, C2PA (JUMBF) and other metadata types for each file format. C2PA metadata is not currently **W**ritable, but may be **D**eleted from some file types by deleting the JUMBF group (ie. `-JUMBF:all=`).

## Installation

Download from [https://exiftool.org/index.html](https://exiftool.org/index.html).


## Basic usage


```
# Print metadata of the file brochure.pdf
exiftool -a -u brochure.pdf
# -a to display duplicated tags
# -u to display unknown tags

# Print common meta information for all images in "dir".  "-common" is a shortcut tag representing common EXIF meta information.
exiftool -common dir

# List specified meta information in tab-delimited column form for all images in "dir" to an output text file named "out.txt".
exiftool -T -createdate -aperture -shutterspeed -iso dir > out.txt

# Print ImageSize and ExposureTime tag names and values.
exiftool -s -ImageSize -ExposureTime b.jpg


# Print standard Canon information from two image files.
exiftool -l -canon c.jpg d.jpg

# Recursively extract common meta information from files in "pictures" directory, writing text output to ".txt" files with the same names.
exiftool -r -w .txt -common pictures

# Save thumbnail image from "image.jpg" to a file called "thumbnail.jpg".
exiftool -b -ThumbnailImage image.jpg > thumbnail.jpg

# Recursively extract JPG image from all Nikon NEF files in the current directory, adding "_JFR.JPG" for the name of the output JPG files.
exiftool -b -JpgFromRaw -w _JFR.JPG -ext NEF -r .

# Extract all types of preview images (ThumbnailImage, PreviewImage, JpgFromRaw, etc.) from files in directory "dir", adding the tag name to the output preview image file names.
exiftool -a -b -W %d%f_%t%-c.%s -preview:all dir

# Print formatted date/time for all JPG files in the current directory.
exiftool -d '%r %a, %B %e, %Y' -DateTimeOriginal -S -s -ext jpg 

# Extract image resolution from EXIF IFD1 information (thumbnail image IFD)
exiftool -IFD1:XResolution -IFD1:YResolution image.jpg

# Extract all tags with names containing the word "Resolution" from an image.
exiftool '-*resolution*' image.jpg

# Extract all author-related XMP information from an image.
exiftool -xmp:author:all -a image.jpg

# Extract complete XMP data record intact from "a.jpg" and write it to "out.xmp" using the special "XMP" tag (see the Extra tags in Image::ExifTool::TagNames).
exiftool -xmp -b a.jpg > out.xmp

```


## Tag names

See table with all tag names: [https://exiftool.org/TagNames/](https://exiftool.org/TagNames/).

A **Tag Name** is the handle by which the information is accessed in ExifTool. 
Tag names are entered on the command line with a leading '`-`', in the order you want them displayed. Valid characters in a tag name are A-Z (case is not significant), 0-9, hyphen (-) and underline (_). The tag name may be prefixed by a [group name](https://exiftool.org/index.html#groups) (separated by a colon) to identify a specific information type or location. A special tag name of "`All`" may be used to represent all tags, or all tags in a specified group. For example:


## Tag groups

See all info related to [Tag groups](https://exiftool.org/index.html#groups)

ExifTool classifies tags into groups in various families. Here is a list of the group names in each family:

|Family|Group Names|
|---|---|
| **0 (Information Type)**|AAC, AFCP, AIFF, APE, APP0, APP1, APP11, APP12, APP13, APP14, APP15, APP2, APP3, APP4, APP5, APP6, APP7, APP8, APP9, ASF, Audible, Canon, CanonVRD, Composite, DICOM, DNG, DV, DjVu, Ducky, EXE, EXIF, ExifTool, FITS, FLAC, FLIR, File, Flash, FlashPix, Font, FotoStation, GIF, GIMP, GeoTiff, GoPro, H264, HTML, ICC_Profile, ID3, IPTC, ISO, ITC, JFIF, JPEG, JSON, JUMBF, Jpeg2000, LNK, Leaf, Lytro, M2TS, MIE, MIFF, MISB, MNG, MOI, MPC, MPEG, MPF, MXF, MakerNotes, Matroska, Meta, Ogg, OpenEXR, Opus, PDF, PICT, PLIST, PNG, PSP, Palm, PanasonicRaw, Parrot, PhotoCD, PhotoMechanic, Photoshop, PostScript, PrintIM, QuickTime, RAF, RIFF, RSRC, RTF, Radiance, Rawzor, Real, Red, SVG, SigmaRaw, Sony, Stim, Theora, Torrent, Trailer, VCard, Vorbis, WTV, XML, XMP, ZIP|
|**1 (Specific Location)**|AAC, AC3, AFCP, AIFF, APE, ASF, AVI1, Adobe, AdobeCM, AdobeDNG, Apple, Audible, CBOR, CIFF, CameraIFD, Canon, CanonCustom, CanonDR4, CanonRaw, CanonVRD, Casio, Chapter#, Composite, DICOM, DJI, DNG, DV, DjVu, DjVu-Meta, Ducky, EPPIM, EXE, EXIF, ExifIFD, ExifTool, FITS, FLAC, FLIR, File, Flash, FlashPix, Font, FotoStation, FujiFilm, FujiIFD, GE, GIF, GIMP, GPS, GSpherical, Garmin, GeoTiff, GlobParamIFD, GoPro, GraphConv, H264, HP, HTC, HTML, HTML-dc, HTML-ncc, HTML-office, HTML-prod, HTML-vw96, HTTP-equiv, ICC-chrm, ICC-clrt, ICC-header, ICC-meas, ICC-meta, ICC-view, ICC_Profile, ICC_Profile#, ID3, ID3v1, ID3v1_Enh, ID3v2_2, ID3v2_3, ID3v2_4, IFD0, IFD1, IPTC, IPTC#, ISO, ITC, InfiRay, Insta360, InteropIFD, ItemList, JFIF, JFXX, JPEG, JPEG-HDR, JPS, JSON, JUMBF, JVC, Jpeg2000, KDC_IFD, Keys, Kodak, KodakBordersIFD, KodakEffectsIFD, KodakIFD, KyoceraRaw, LNK, Leaf, LeafSubIFD, Leica, Lyrics3, Lytro, M-RAW, M2TS, MAC, MIE-Audio, MIE-Camera, MIE-Canon, MIE-Doc, MIE-Extender, MIE-Flash, MIE-GPS, MIE-Geo, MIE-Image, MIE-Lens, MIE-Main, MIE-MakerNotes, MIE-Meta, MIE-Orient, MIE-Preview, MIE-Thumbnail, MIE-UTM, MIE-Unknown, MIE-Video, MIFF, MISB, MNG, MOBI, MOI, MPC, MPEG, MPF0, MPImage, MS-DOC, MXF, MacOS, MakerNotes, MakerUnknown, Matroska, MediaJukebox, Meta, MetaIFD, Microsoft, Minolta, MinoltaRaw, Motorola, NITF, Nikon, NikonCapture, NikonCustom, NikonScan, NikonSettings, NineEdits, Nintendo, Ocad, Ogg, Olympus, OpenEXR, Opus, PDF, PICT, PNG, PNG-cICP, PNG-pHYs, PSP, Palm, Panasonic, PanasonicRaw, Parrot, Pentax, PhaseOne, PhotoCD, PhotoMechanic, Photoshop, PictureInfo, PostScript, PreviewIFD, PrintIM, ProfileIFD, Qualcomm, QuickTime, RAF, RAF2, RIFF, RMETA, RSRC, RTF, Radiance, Rawzor, Real, Real-CONT, Real-MDPR, Real-PROP, Real-RA3, Real-RA4, Real-RA5, Real-RJMD, Reconyx, Red, Ricoh, SPIFF, SR2, SR2DataIFD, SR2SubIFD, SRF#, SVG, Samsung, Sanyo, Scalado, Sigma, SigmaRaw, Sony, SonyIDC, Stim, SubIFD, System, Theora, Torrent, Track#, UserData, VCalendar, VCard, VNote, Version0, Vorbis, WTV, XML, XMP, XMP-DICOM, XMP-Device, XMP-GAudio, XMP-GCamera, XMP-GCreations, XMP-GDepth, XMP-GFocus, XMP-GImage, XMP-GPano, XMP-GSpherical, XMP-LImage, XMP-MP, XMP-MP1, XMP-PixelLive, XMP-aas, XMP-acdsee, XMP-album, XMP-apple-fi, XMP-ast, XMP-aux, XMP-cc, XMP-cell, XMP-crd, XMP-creatorAtom, XMP-crs, XMP-dc, XMP-dex, XMP-digiKam, XMP-drone-dji, XMP-dwc, XMP-et, XMP-exif, XMP-exifEX, XMP-expressionmedia, XMP-extensis, XMP-fpv, XMP-getty, XMP-hdr, XMP-hdrgm, XMP-ics, XMP-iptcCore, XMP-iptcExt, XMP-lr, XMP-mediapro, XMP-microsoft, XMP-mwg-coll, XMP-mwg-kw, XMP-mwg-rs, XMP-nine, XMP-panorama, XMP-pdf, XMP-pdfx, XMP-photomech, XMP-photoshop, XMP-plus, XMP-pmi, XMP-prism, XMP-prl, XMP-prm, XMP-pur, XMP-rdf, XMP-sdc, XMP-swf, XMP-tiff, XMP-x, XMP-xmp, XMP-xmpBJ, XMP-xmpDM, XMP-xmpDSA, XMP-xmpMM, XMP-xmpNote, XMP-xmpPLUS, XMP-xmpRights, XMP-xmpTPg, ZIP, iTunes|
|**2 (Category)**|Audio, Author, Camera, Device, Document, ExifTool, Image, Location, Other, Preview, Printing, Time, Unknown, Video|
|**3 (Document Number)**|Doc#, Main|
|**4 (Instance Number)**|Copy#|
|**5 (Metadata Path)**|eg. JPEG-APP1-IFD0-ExifIFD|
|**6 (EXIF/TIFF Format)**|int8u, string, int16u, int32u, rational64u, int8s, undef, int16s, int32s, rational64s, float, double, ifd, unicode, complex, int64u, int64s, ifd64|
|**7 (Tag ID)**|ID-xxx (where xxx is the tag ID. Numerical ID's are given in hex with a leading "0x" if the [HexTagIDs API option](https://exiftool.org/ExifTool.html#HexTagIDs) is set, as are characters in non-numerical ID's which are not valid in a group name. Note that unlike other group names, family 7 group names are case sensitive.)|
|**8 (File Number)**|File# (for files loaded via `-file_NUM_` option)|

The exiftool output can be organized based on these groups using the `-g` or `-G` option (ie. `-g1` to see family 1 groups, or `-g3:1` to see both family 3 and family 1 group names in the output. See the `-g` option in the exiftool application documentation for more details, and the [GetGroup](https://exiftool.org/ExifTool.html#GetGroup) function in the ExifTool library for a description of the group families. Note that when writing, only family 0, 1, 2 and 7 group names may be used.