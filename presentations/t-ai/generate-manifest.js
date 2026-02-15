#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const PDF_DIR = path.join(__dirname, 'pdf');
const MANIFEST_PATH = path.join(PDF_DIR, 'manifest.json');

function generateManifest() {
  if (!fs.existsSync(PDF_DIR)) {
    console.error(`Папка ${PDF_DIR} не найдена`);
    process.exit(1);
  }

  const files = fs.readdirSync(PDF_DIR)
    .filter(name => /\.pdf$/i.test(name) && name !== 'manifest.json')
    .map(name => {
      const filePath = path.join(PDF_DIR, name);
      const stats = fs.statSync(filePath);
      
      return {
        name,
        size: stats.size,
        modified: stats.mtime.toISOString()
      };
    })
    .sort((a, b) => a.name.localeCompare(b.name, 'ru'));

  const manifest = {
    generated: new Date().toISOString(),
    files
  };

  fs.writeFileSync(MANIFEST_PATH, JSON.stringify(manifest, null, 2), 'utf-8');
  console.log(`✓ Манифест создан: ${files.length} файлов`);
  files.forEach(f => console.log(`  - ${f.name} (${(f.size / 1024 / 1024).toFixed(2)} MB)`));
}

generateManifest();
