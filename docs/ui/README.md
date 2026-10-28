# UI previews

These screenshots were captured from the running application using the saved thesis results:

- [Dataset overview](overview.png): model selection, structural summaries for 188 repositories, documentation summaries for the 30-repository annotated corpus, model agreement metrics, and the repository browser.
- [Individual repository report](repository-report.png): the saved Astropy hybrid profile, with the installation explanation expanded.
- [Model comparison](model-comparison.png): saved Llama and Qwen assessments for Astropy, human reference scores, and highlighted model disagreements.
- [Repository submission](assess-repository.png): the form for requesting a new assessment with Qwen through KISTE selected.

The submission screenshot shows the input feature; it does not claim a completed live assessment. For the defense, saved reports and comparisons work without GitHub, Ollama, or KISTE. New assessments require GitHub connectivity and, when documentation scoring is selected, the chosen Ollama or KISTE service. KISTE configuration status does not verify a working connection or token.

The browser smoke test in `code/web/tests/browser_smoke.mjs` refreshes these images. Screenshots are not automatically inserted into the thesis.

Last refreshed and visually checked: **2026-09-26**. The browser smoke test passed against the current local app, including model switching, saved scores, filters, mobile layout, and failure states.

## Refresh after UI changes

Regenerate these previews whenever the frontend or displayed results change, review the images, and commit them alongside the relevant changes. This is a manual workflow; screenshots are not automatically refreshed by CI.

With the Python environment activated, project dependencies installed, Node.js 22+ and Chrome available, run these commands from the repository root:

1. Start the app in one terminal:

   ```sh
   python -m uvicorn main:app --app-dir code/web/backend --host 127.0.0.1 --port 8765
   ```

2. Launch a separate headless Chrome instance. In Windows PowerShell:

   ```powershell
   $previewProfile = Join-Path $env:TEMP ('fairness-ui-' + [guid]::NewGuid().ToString())
   $previewBrowser = Start-Process -FilePath 'C:\Program Files\Google\Chrome\Application\chrome.exe' -ArgumentList @('--headless=new', '--remote-debugging-port=9223', ('--user-data-dir="' + $previewProfile + '"'), '--no-first-run', '--no-default-browser-check', 'about:blank') -WindowStyle Hidden -PassThru
   ```

   On other systems, launch Chrome with the same flags and a new temporary profile directory, using its local executable path.

3. Run the capture and checks:

   ```sh
   node code/web/tests/browser_smoke.mjs
   ```

4. Confirm the script prints `PASS`, open all four PNGs to check their content and layout, and update the refresh date above. The script overwrites images as it runs, so a failed run may leave only some previews refreshed; rerun successfully before committing.

5. Stop the app with Ctrl+C. Close the dedicated browser in the PowerShell terminal used to launch it:

   ```powershell
   Stop-Process -Id $previewBrowser.Id
   ```

The capture uses saved results and mocks assessment responses for failure checks; it does not perform live model inference. These four previews cover selected views, not every page. Thesis screenshots in `thesis/figures/ui/` are maintained separately.
