try:
    from PIL import Image
except ImportError:
    def notify_pillow_missing():
        bpy.ops.error.message('INVOKE_DEFAULT', message="Pillow library is not installed. Please install Pillow.")
    
    class ERROR_OT_message(bpy.types.Operator):
        bl_idname = "error.message"
        bl_label = "Error"
        message: bpy.props.StringProperty()

        def execute(self, context):
            self.report({'ERROR'}, self.message)
            return {'FINISHED'}

    def register():
        bpy.utils.register_class(ERROR_OT_message)
        notify_pillow_missing()
    
    def unregister():
        bpy.utils.unregister_class(ERROR_OT_message)
    
    if __name__ == "__main__":
        register()

else:
    # Pillowがインストールされている場合、通常のアドオン機能を実行する
    class ConvertTexturesToWebP(bpy.types.Operator):
        bl_idname = "object.convert_textures_to_webp"
        bl_label = "Convert Textures to WebP"
        bl_description = "Convert all textures to WebP format"
        bl_options = {'REGISTER', 'UNDO'}

        def execute(self, context):
            materials = bpy.data.materials
            
            for mat in materials:
                if mat.node_tree:
                    for node in mat.node_tree.nodes:
                        if node.type == 'TEX_IMAGE':
                            image = node.image
                            if image:
                                self.convert_to_webp(image)
            
            return {'FINISHED'}

        def convert_to_webp(self, image):
            file_path = bpy.path.abspath(image.filepath)
            if os.path.exists(file_path):
                img = Image.open(file_path)
                webp_path = os.path.splitext(file_path)[0] + ".webp"
                img.save(webp_path, format="WEBP")
                image.filepath = webp_path
                image.reload()
                print(f"Converted {file_path} to {webp_path}")

    def menu_func(self, context):
        self.layout.operator(ConvertTexturesToWebP.bl_idname)

    def register():
        bpy.utils.register_class(ConvertTexturesToWebP)
        bpy.types.TOPBAR_MT_file.append(menu_func)

    def unregister():
        bpy.utils.unregister_class(ConvertTexturesToWebP)
        bpy.types.TOPBAR_MT_file.remove(menu_func)

    if __name__ == "__main__":
        register()
