# README insertion

Insert this at the desired location in the repository-root README.md. Paths below are relative to that file.

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-vector-20260914/banner/readme-banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/logo-vector-20260914/banner/readme-banner-light.svg">
  <img src="assets/logo-vector-20260914/banner/readme-banner-light.svg" alt="Vietnam Business Law Practitioner" width="100%">
</picture>
```

For a single fixed light-background PNG:

```markdown
![Vietnam Business Law Practitioner](assets/logo-vector-20260914/banner/readme-banner-light.png)
```

For the standalone symbol, use `assets/logo-vector-20260914/svg/symbol-color.svg` on light backgrounds or `symbol-white.svg` from the same folder on dark backgrounds.

