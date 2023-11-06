# rpm-specs
A repository for all the RPM .spec files that I maintain (primarily on Fedora COPR).

The packages are automatically updated by a [script](/update.sh) that fetches the latest releases from the GitHub API.\
The script is ran by GitHub actions every 12 hours.

If anything is wrong with the packages, please [create an issue](https://github.com/ErrorNoInternet/rpm-specs/issues/new) (or [submit a pull request](https://github.com/ErrorNoInternet/rpm-specs/compare)).\
Any modifications to the COPR pages may also be requested by [creating an issue](https://github.com/ErrorNoInternet/rpm-specs/issues/new) here.

## Fedora Packages
- [libsixel](https://github.com/libsixel/libsixel): SIXEL encoding and decoding ([Fedora RPMs](https://src.fedoraproject.org/rpms/libsixel))
- [qoi](https://github.com/phoboslab/qoi): The "Quite OK Image Format" for fast, loseless image compression ([Fedora RPMs](https://src.fedoraproject.org/rpms/qoi))

## COPR Packages
- [7zip](https://7-zip.org): A file archiver with a high compression ratio ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/7zip))
- [klassy](https://github.com/paulmcauley/klassy): A highly customizable KDE Plasma Window Decoration ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/klassy))
- kwin-effects ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/kwin-effects)):
  - (Plasma 5.27.6) [kwin-effects-sliding-notifications](https://github.com/zzag/kwin-effects-sliding-notifications): Sliding animation for notification windows ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/kwin-effects/package/kwin-effects-sliding-notifications))
~~- [libsixel](https://github.com/libsixel/libsixel): SIXEL encoding and decoding ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/libsixel))~~
- [mergerfs](https://github.com/trapexit/mergerfs): A featureful FUSE based union filesystem ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/mergerfs))
- [par2cmdline-turbo](https://github.com/animetosho/par2cmdline-turbo): par2cmdline × ParPar: speed focused par2cmdline fork ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/par2cmdline-turbo))
~~- [qoi](https://github.com/phoboslab/qoi)(-devel): The "Quite OK Image Format" for fast, loseless image compression ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/qoi))~~
- [timg](https://github.com/hzeller/timg): A terminal image and video viewer ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/timg))
- [try](https://github.com/binpash/try): Inspect a command's effects before modifying your live system ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/try))
