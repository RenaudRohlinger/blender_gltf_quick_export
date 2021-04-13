# by Renaud ROHLINGER
import bpy
import os

def main(context):

    # name of the glb generated based on the name of the .blend file
    basedir = os.path.dirname(bpy.data.filepath)
    name = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
    fn = os.path.join(basedir, name)
    print(basedir, name, fn)


    #export glb in the same folder as the blend file
    bpy.ops.export_scene.gltf(
        filepath=fn + ".glb",
        export_format='GLB'
    )
    pass


class SimpleOperator(bpy.types.Operator):
        bl_idname = "object.simple_operator"
        bl_label = "Quick Export"
       
        def execute(self, context):
            try:
                main(context)
                return {'FINISHED'}
            except Exception as e:
                print("something went wrong")
                #raise the exception again
                raise e




class HelloWorldPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = 'GLTF'
    bl_label = "GLTF Quick Export"

    def draw(self, context):
        layout = self.layout

        obj = context.object
       
        layout.operator('object.simple_operator')


def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(HelloWorldPanel)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(HelloWorldPanel)

if __name__ == "__main__":
    register()
