"""
HTML templates
"""

from string import Template
from . import util

article = Template(util.dedent("""
    <article style="margin: 5px; clear: both; overflow: auto; padding: 10px; border: 1px solid var(--border-color-primary, #ccc); border-radius: 8px; background: var(--background-fill-secondary, #f5f5f5);">
        $thumbnail
        <div style="font-size:16px">
            File: $model_path
        </div>
        $download
        <div style="font-size:20px;margin:6px 0px;">
            <b>Model: <a href="$url" target="_blank"><u>$model_name</u></a></b>
        </div>
    </article>
""").strip())

thumbnail = Template(util.dedent("""
    <img src='$img_url' style='float: left; margin: 5px; max-width: 200px; max-height: 200px; object-fit: contain;'>
""").strip())

description = Template(util.dedent("""
    <blockquote style="font-size:16px;margin:6px 0px;">
        $description
    </blockquote>
    <br>
""").strip())

# add js function to download new version into SD webui by python
# in embed HTML, onclick= will also follow a ", never a ',
# so have to write it as following
download = Template(util.dedent("""
    <div style="font-size:16px;margin:6px 0px;">
        New Version: <u><a href="$download_url" target="_blank" style="margin:0px 10px;">$new_version_name</a></u>
        <u><a href='#' style='margin:0px 10px;' onclick="ch_dl_model_new_version(event, '$model_path', '$new_version_id', '$download_url', '$model_type')">[Download into SD]</a></u>
    </div>
""").strip())

no_download = Template(util.dedent("""
    <div style="font-size:16px;margin:6px 0px;">
        New Version: $new_version_name
    </div>
""").strip())

duplicate_card = Template(util.dedent("""
    <a href='#' onclick="remove_dup_card(event, '$model_type', '$search_term')" onmouseover="display_ch_path(event, '$path')" onmouseout="hide_ch_path(event)" onmousemove="move_ch_path(event)">
        <div class='card' style=$style data-name="$name">
            $background_image
            <div class='actions'>
                <div class='additional'>
                    <span style="display:none">$search_term</span>
                </div>
                <span class='name'>$name</span>
                <span class='description'>$description</span>
            </div>
        </div>
    </a>
""").strip())

duplicate_preview = Template(util.dedent("""
    <img src="./sd_extra_networks/thumb?filename=$bg_image" class="preview" loading="lazy">
""").strip())

duplicate_article = Template(util.dedent("""
    <article>
        <h1>
            $section_name
        </h1>
        $contents
    </article>
""").strip())

duplicate_row = Template(util.dedent("""
    <div id="ch_$hash">
        <div class=civitai_name>
            <h2>
                $civitai_name
            </h2>
        </div>
        <div class=duplicate_model id="ch_${hash}_cards">
            $columns
        </div>
    </div>
""").strip())


duplicate_column = Template(util.dedent("""
        <div class=dup_$count>
            $card
        </div>
""").strip())

# New table-based templates for duplicate scan
duplicate_table_wrapper = Template(util.dedent("""
    <div class="ch_dup_table_wrapper">
        <h2>$civitai_name <span class="ch_hash_label">(Hash: $hash)</span></h2>
        <table class="ch_dup_table">
            <thead>
                <tr>
                    <th>Image</th>
                    <th>Name</th>
                    <th>Version</th>
                    <th>Base Model</th>
                    <th>Path</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                $rows
            </tbody>
        </table>
    </div>
""").strip())

duplicate_table_row = Template(util.dedent("""
    <tr>
        <td class="ch_dup_img">$preview_img</td>
        <td class="ch_dup_name">$model_name</td>
        <td class="ch_dup_version">$version</td>
        <td class="ch_dup_base">$base_model</td>
        <td class="ch_dup_path" title="$full_path">$short_path</td>
        <td class="ch_dup_actions">
            <a href='#' class="ch_delete_btn" onclick="remove_dup_card(event, '$model_type', '$search_term')" title="Delete model and all associated files">
                🗑️ Delete
            </a>
        </td>
    </tr>
""").strip())

duplicate_table_preview = Template(util.dedent("""
    <img src="./sd_extra_networks/thumb?filename=$bg_image" loading="lazy">
""").strip())

duplicate_table_section = Template(util.dedent("""
    <div class="ch_dup_section">
        <h1>$section_name</h1>
        $contents
    </div>
""").strip())
