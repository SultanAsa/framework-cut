<div align="center">

<img src="assets/frameworkcut_logo_512.png" alt="FrameWork Cut" width="110" />

# FrameWork Cut

**A free, local video editor. No watermarks, no account, no subscription.**

</div>

---

## About

FrameWork Cut is a desktop video editor that runs entirely on your own machine.
Multi-track timeline, cutting, transitions, titles, captions and export — with
nothing uploaded anywhere and nothing to sign up for.

It ships alongside [FrameWork Boost](https://framework.shop), which can install
and launch it for you, but it is a complete application on its own and runs
perfectly well without it.

## This is a fork

FrameWork Cut is a fork of **[Concat](https://github.com/jub0t/Concat)** by
Jareer ([@jub0t](https://github.com/jub0t)) and the Concat contributors, used
under the AGPL-3.0-or-later.

This build carries its own name and icon, as Concat's trademark policy asks of
modified builds. It is **not** official Concat, and the Concat project does not
maintain it or take bug reports for it — please report anything you find here,
at [this repository's issues](https://github.com/SultanAsa/framework-cut/issues).

Changes in this fork, so far:

- Renamed and re-iconed as FrameWork Cut.
- Windows x86_64 only, to match the product it ships beside.

Everything else is upstream's work, and upstream deserves the credit for it.

## Licence

**AGPL-3.0-or-later**, the same as upstream — see [`LICENSE`](LICENSE), and
[`LICENSE-EXCEPTIONS.md`](LICENSE-EXCEPTIONS.md) for the plugin exception that
comes with it. The full source of this fork is this repository.

Third-party components and their licences: [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

The FrameWork name and logo are not covered by that licence. Concat's name and
logo are its project's, and are used here only to say what this is a fork of.

## Building

Needs the Rust toolchain, the FFmpeg 8 development libraries, CMake, a C++
toolchain and libclang. `.github/workflows/build-app.yml` is the authoritative
description of the build environment.

```
cd src
cargo build --profile app -p concat
```
