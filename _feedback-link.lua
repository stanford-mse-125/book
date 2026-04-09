function Pandoc(doc)
  local input = quarto.doc.input_file
  if not input then return doc end
  local base = input:match("([^/]+)%.qmd$")
  if not base or not (base:match("^lec%d") or base:match("^appendix%-")) then return doc end

  -- Extract chapter number from filename (e.g., "lec03-data-munging" -> "3")
  -- For appendix files, use the appendix name (e.g., "appendix-probability" -> "appendix-probability")
  local num = base:match("^lec(%d+)")
  if num then
    num = tostring(tonumber(num))  -- strip leading zero
  elseif base:match("^appendix%-") then
    num = base
  end

  local form_url = "https://docs.google.com/forms/d/e/1FAIpQLScokCu2Rsz7zZw7XTOzsE_OBODr6iHjB1ErOw0zizorHD0zXg/viewform"
    .. "?usp=pp_url"
    .. "&entry.1875336381=Course+Notes"
    .. "&entry.1608396530=" .. (num or "")

  local feedback_html = '<div class="feedback-link" style="margin-top: 2em; padding: 0.75em 1em; background: #f0f7f5; border-left: 4px solid #5ba899; border-radius: 6px; font-size: 0.9em;">'
    .. 'How was this chapter? Help us improve these notes. '
    .. '<a href="' .. form_url .. '" target="_blank" style="color: #3d7a6e; font-weight: 500;">Share feedback</a>'
    .. '</div>'

  local block = pandoc.RawBlock("html", feedback_html)
  table.insert(doc.blocks, block)
  return doc
end
