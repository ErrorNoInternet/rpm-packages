# rpm-specs
A repository for all the RPM .spec files that I maintain (primarily on Fedora COPR).

The packages are automatically updated by running a [script](/update.sh) that uses the GitHub API to fetch the latest releases from each repository.\
The script is ran by GitHub actions every 12 hours.

If anything is wrong with the packages, please [create an issue](https://github.com/ErrorNoInternet/rpm-specs/issues/new) (or [submit a pull request](https://github.com/ErrorNoInternet/rpm-specs/compare)).\
Any modifications to the COPR pages may also be requested by [creating an issue](https://github.com/ErrorNoInternet/rpm-specs/issues/new) here.

## Packages
- kwin-effects ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/kwin-effects)):
  - [kwin-effects-sliding-notifications](https://github.com/zzag/kwin-effects-sliding-notifications): Sliding animation for notification windows ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/kwin-effects/package/kwin-effects-sliding-notifications))
- [timg](https://github.com/hzeller/timg): A terminal image and video viewer ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/timg))
- [klassy](https://github.com/paulmcauley/klassy): A highly customizable KDE Plasma Window Decoration ([COPR](https://copr.fedorainfracloud.org/coprs/errornointernet/klassy))
