#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils:../../../hardware/oplus/extract-utils-ext python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils_oplus import (
    add_generated_thermal_engine_config,
)

namespace_imports = [
    'hardware/oplus',
    'hardware/pixelworks/interfaces',
    'hardware/qcom-caf/sm8650',
    'vendor/oneplus/sm8650-common',
    'vendor/qcom/opensource/commonsys-intf/display',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qti.sensor.lyt808',
        'libarcsoft_triple_sat',
        'libdualcam_video_optical_zoom',
        'libhwconfigurationutil',
        'libpwirisfeature',
        'libpwirishalwrapper',
        'libtriplecam_video_optical_zoom',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'odm/etc/camera/CameraHWConfiguration.config': blob_fixup()
        # Disable face detection AE behaviour
        .regex_replace(r'(enableSWfdForThirdCamUnit += )TRUE', r'\1FALSE')
        .regex_replace(r'(fdSupport += )TRUE;', r'\1FALSE;')
        # Expose AUX cameras
        .regex_replace('SystemCamera =  0;  0;  0;  1;  0; 1;', 'SystemCamera =  0;  0;  0;  0;  0; 0;'),
    (
        'odm/etc/libnfc-mtp-SN220.conf_22825',
        'odm/etc/libnfc-mtp-SN220.conf_22877',
    ): blob_fixup()
        .regex_replace('(NXPLOG_.*_LOGLEVEL)=0x03', '\\1=0x02')
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),
    (
        'odm/lib64/camera/com.qti.sensor.imx581.so',
        'odm/lib64/camera/com.qti.sensor.imx615.so',
        'odm/lib64/camera/com.qti.sensor.imx888.so',
        'odm/lib64/camera/com.qti.sensor.lyt808.so',
        'odm/lib64/camera/com.qti.sensor.ov64b40_tele.so',
        'odm/lib64/libextensionlayer.so',
        'vendor/lib64/camera/com.qti.eeprom.gt24p128c2csli_imx766.so',
        'vendor/lib64/camera/com.qti.eeprom.gt24p128e2csli_s5kjn1.so',
        'vendor/lib64/camera/com.qti.eeprom.irs2381c_polar.so',
        'vendor/lib64/camera/com.qti.eeprom.truly_cmb433.so',
        'vendor/lib64/camera/com.qti.ois.bu63169gwz.so',
        'vendor/lib64/camera/com.qti.ois.dw9784.so',
        'vendor/lib64/camera/com.qti.sensor.imx362.so',
        'vendor/lib64/camera/com.qti.sensor.imx363.so',
        'vendor/lib64/camera/com.qti.sensor.imx376.so',
        'vendor/lib64/camera/com.qti.sensor.imx386.so',
        'vendor/lib64/camera/com.qti.sensor.imx476.so',
        'vendor/lib64/camera/com.qti.sensor.imx481.so',
        'vendor/lib64/camera/com.qti.sensor.imx519.so',
        'vendor/lib64/camera/com.qti.sensor.imx563.so',
        'vendor/lib64/camera/com.qti.sensor.imx576.so',
        'vendor/lib64/camera/com.qti.sensor.imx586.so',
        'vendor/lib64/camera/com.qti.sensor.imx588.so',
        'vendor/lib64/camera/com.qti.sensor.imx686.so',
        'vendor/lib64/camera/com.qti.sensor.imx688.so',
        'vendor/lib64/camera/com.qti.sensor.imx766.so',
        'vendor/lib64/camera/com.qti.sensor.lyt808.so',
        'vendor/lib64/camera/com.qti.sensor.max7366_6dof.so',
        'vendor/lib64/camera/com.qti.sensor.max7366_eyetrack.so',
        'vendor/lib64/camera/com.qti.sensor.max7366_ov6211.so',
        'vendor/lib64/camera/com.qti.sensor.max7366_ov9282.so',
        'vendor/lib64/camera/com.qti.sensor.ov13855.so',
        'vendor/lib64/camera/com.qti.sensor.ov64b40.so',
        'vendor/lib64/camera/com.qti.sensor.ov7251.so',
        'vendor/lib64/camera/com.qti.sensor.s5k2l7.so',
        'vendor/lib64/camera/com.qti.sensor.s5k2x5sp.so',
        'vendor/lib64/camera/com.qti.sensor.s5k33dxx.so',
        'vendor/lib64/camera/com.qti.sensor.s5k3m5.so',
        'vendor/lib64/camera/com.qti.sensor.s5k3p9.so',
        'vendor/lib64/camera/com.qti.sensor.s5k4h7.so',
        'vendor/lib64/camera/com.qti.sensor.s5k5e9yu05.so',
        'vendor/lib64/camera/com.qti.sensor.s5k5e9yx04.so',
        'vendor/lib64/camera/com.qti.sensor.s5khp1s.so',
        'vendor/lib64/camera/com.qti.sensor.s5kjd1sp.so',
        'vendor/lib64/camera/com.qti.sensor.s5kjn1.so',
        'vendor/lib64/camera/components/com.qti.node.aon.so',
        'vendor/lib64/camera/components/com.qti.node.depth.so',
        'vendor/lib64/camera/components/com.qti.node.depthprovider.so',
        'vendor/lib64/camera/components/com.qti.node.dewarp.so',
        'vendor/lib64/camera/components/com.qti.node.eisv2.so',
        'vendor/lib64/camera/components/com.qti.node.eisv3.so',
        'vendor/lib64/camera/components/com.qti.node.evadepth.so',
        'vendor/lib64/camera/components/com.qti.node.gme.so',
        'vendor/lib64/camera/components/com.qti.node.gyrornn.so',
        'vendor/lib64/camera/components/com.qti.node.hdr10pgen.so',
        'vendor/lib64/camera/components/com.qti.node.hdr10phist.so',
        'vendor/lib64/camera/components/com.qti.node.itofpreprocess.so',
        'vendor/lib64/camera/components/com.qti.node.ml.so',
        'vendor/lib64/camera/components/com.qti.node.mlinference.so',
        'vendor/lib64/camera/components/com.qti.node.seg.so',
        'vendor/lib64/camera/components/com.qti.node.swec.so',
        'vendor/lib64/camera/components/com.qti.node.swregistration.so',
        'vendor/lib64/camera/components/com.qti.stats.cnndriver.so',
        'vendor/lib64/camera/components/libcamxevainterface.so',
        'vendor/lib64/camera/components/libdepthmapwrapper_itof.so',
        'vendor/lib64/camera/components/libdepthmapwrapper_secure.so',
        'vendor/lib64/com.qti.camx.chiiqutils.so',
        'vendor/lib64/com.qti.chiusecaseselector.so',
        'vendor/lib64/com.qti.feature2.afbrckt.so',
        'vendor/lib64/com.qti.feature2.anchorsync.so',
        'vendor/lib64/com.qti.feature2.demux.so',
        'vendor/lib64/com.qti.feature2.derivedoffline.so',
        'vendor/lib64/com.qti.feature2.fusion.so',
        'vendor/lib64/com.qti.feature2.generic.so',
        'vendor/lib64/com.qti.feature2.gs.sm8650.so',
        'vendor/lib64/com.qti.feature2.hdr.so',
        'vendor/lib64/com.qti.feature2.mcreprocrt.so',
        'vendor/lib64/com.qti.feature2.memcpy.so',
        'vendor/lib64/com.qti.feature2.metadataserializer.so',
        'vendor/lib64/com.qti.feature2.mfsr.so',
        'vendor/lib64/com.qti.feature2.ml.so',
        'vendor/lib64/com.qti.feature2.mux.so',
        'vendor/lib64/com.qti.feature2.qcfa.so',
        'vendor/lib64/com.qti.feature2.rawhdr.so',
        'vendor/lib64/com.qti.feature2.realtimeserializer.so',
        'vendor/lib64/com.qti.feature2.rt.so',
        'vendor/lib64/com.qti.feature2.rtmcx.so',
        'vendor/lib64/com.qti.feature2.serializer.so',
        'vendor/lib64/com.qti.feature2.statsregeneration.so',
        'vendor/lib64/com.qti.feature2.stub.so',
        'vendor/lib64/com.qti.feature2.swmf.so',
        'vendor/lib64/com.qti.qseeutils.so',
        'vendor/lib64/com.qualcomm.mcx.distortionmapper.so',
        'vendor/lib64/com.qualcomm.mcx.linearmapper.so',
        'vendor/lib64/com.qualcomm.mcx.nonlinearmapper.so',
        'vendor/lib64/com.qualcomm.mcx.policy.mfl.so',
        'vendor/lib64/com.qualcomm.qti.mcx.usecase.extension.so',
        'vendor/lib64/hw/camera.qcom.sm8650.so',
        'vendor/lib64/hw/camera.qcom.so',
        'vendor/lib64/hw/com.qti.chi.offline.so',
        'vendor/lib64/hw/com.qti.chi.override.so',
        'vendor/lib64/libcamerapostproc.so',
        'vendor/lib64/libcamxhwnodecontext.so',
        'vendor/lib64/libcamxifestriping.so',
        'vendor/lib64/libcamximageformatutils.so',
        'vendor/lib64/libcamxncsdatafactory.so',
        'vendor/lib64/libchifeature2.so',
        'vendor/lib64/libcommonchiutils.so',
        'vendor/lib64/libipebpsstriping.so',
        'vendor/lib64/libipebpsstriping170.so',
        'vendor/lib64/libipebpsstriping480.so',
        'vendor/lib64/libisphwsetting.so',
        'vendor/lib64/libjpege.so',
        'vendor/lib64/libmctfengine_stub.so',
        'vendor/lib64/libmfec.so',
        'vendor/lib64/libmmcamera_bestats.so',
        'vendor/lib64/libmmcamera_cac.so',
        'vendor/lib64/libmmcamera_lscv35.so',
        'vendor/lib64/libmmcamera_pdpc.so',
        'vendor/lib64/libmmcamera_pnc.so',
        'vendor/lib64/libopestriping.so',
        'vendor/lib64/libtfestriping.so',
        'vendor/lib64/libubifocus.so',
        'vendor/lib64/vendor.oplus.hardware.camera.aon-service-impl.so',
        'vendor/lib64/vendor.qti.hardware.camera.aon-service-impl.so',
        'vendor/lib64/vendor.qti.hardware.camera.offlinecamera-service-impl.so',
        'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so',
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so'),
    (
        'odm/lib64/libSuperRaw.so',
    ): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    (
        'odm/lib64/libdisplaycolorfeature.so',
        'odm/lib64/libdisplayfossfeature_nature.so',
        'vendor/lib64/libdpps.so',
        'vendor/lib64/libsnapdragoncolor-manager.so',
    ): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    (
        'odm/lib64/libEIS.so',
        'odm/lib64/libHIS.so',
        'odm/lib64/libOGLManager.so',
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'vendor/etc/libnfc-nci.conf': blob_fixup()
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),
    'vendor/lib64/libcamera2ndk_vendor.so': blob_fixup()
        .replace_needed('android.frameworks.cameraservice.device-V1-ndk.so', 'android.frameworks.cameraservice.device-V3-ndk.so')
        .replace_needed('android.frameworks.cameraservice.service-V1-ndk.so', 'android.frameworks.cameraservice.service-V3-ndk.so'),
    (
        'odm/lib64/libpwirishalwrapper.so',
        'vendor/lib64/libpwirishalwrapper.so',
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.composer3-V2-ndk.so', 'android.hardware.graphics.composer3-V3-ndk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'waffle',
    'oneplus',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

add_generated_thermal_engine_config(
    module,
    horae_target_config='system_ext/etc/horae/horae_SM8650.conf',
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8650-common', module.vendor
    )
    utils.run()
