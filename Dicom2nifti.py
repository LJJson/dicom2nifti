import dicom2nifti
import SimpleITK as sitk

if __name__ == '__main__':
    dicom_path = "./data/4_579E62D1A4D3455DA93951801FA6F03A"
    path1 = 'data/7_53ADDBD8A08A48AEBABF593C4349C793'
    dicom2nifti.convert_directory(path1, './nii_output')
    source = sitk.ReadImage('nii_output/7_t1_tse_tra.nii.gz')
    source1= sitk.ReadImage('nii_output/4_t1_tse_cor.nii.gz')
    print(source1.GetSize())
    print(source.GetSize())



