function Pandoc(doc)
  local input = quarto.doc.input_file
  if not input then return doc end
  local base = input:match("([^/]+)%.qmd$")
  if not base or not base:match("^lec%d") then return doc end

  local form_url = "https://forms.gle/PLACEHOLDER?entry.NNNN=" .. base

  local feedback_html = '<div class="feedback-link" style="margin-top: 2em; padding: 0.75em 1em; background: #f0f7f5; border-left: 4px solid #5ba899; border-radius: 6px; font-size: 0.9em;">'
    .. 'How was this chapter? Help us improve these notes. '
    .. '<a href="' .. form_url .. '" target="_blank" style="color: #3d7a6e; font-weight: 500;">Share feedback</a>'
    .. '</div>'

  local block = pandoc.RawBlock("html", feedback_html)
  table.insert(doc.blocks, block)
  return doc
end
