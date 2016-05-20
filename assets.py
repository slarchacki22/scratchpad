<html metal:use-macro="view.global_template">
    <tal:block metal:fill-slot="body">
        <div class="container">
            <section>
                <h1>Asssets</h1>
                <div tal:repeat="assets view.get_assets_list" >
                    <img src="images/${ assets['name']}" />
                        <p>${ assets['name'] }</p>

                </div>
            </section>
        </div>
    </tal:block>
</html>
